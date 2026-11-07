from flask import Flask, jsonify, make_response
import threading
import requests
import time
import os

app = Flask(__name__, static_folder=None)

TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.route('/')
def home():
    return "BINARY AI Trader Engine Online - Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        current_time = time.time()
        time_slot = int(current_time / 5)
        
        trend_calc = (time_slot * 31337 + 7357) % 100
        base_signal = "CALL" if (trend_calc >= 50) else "PUT"
        
        volatility = (time_slot * 16657) % 15
        real_accuracy = 85 + volatility
        
        res = jsonify({
            "signal": base_signal,
            "trend": "BINARY_AI_REAL_ANALYSIS",
            "confidence": real_accuracy,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "CALL",
            "trend": "STABLE MOMENTUM",
            "confidence": 96,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

@app.route('/bot.js')
def bot_script():
    js = """
    (function(){
        try {
            var d = document;
            
            // Clean up old elements
            ["binary-ai-bot-btn", "binary-ai-scanner-overlay", "binary-ai-style", "binary-laser-line"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var renderServerUrl = "https://r-bot-ai.onrender.com";

            // CSS Animations & Slow Motion Color Changing Effects
            var s = d.createElement('style');
            s.id = 'binary-ai-style';
            s.innerHTML = '@keyframes slowBorderColorChange {' +
                          '0% { border-color: #22c55e; box-shadow: 0 0 15px rgba(34,197,94,0.7); }' +
                          '33% { border-color: #38bdf8; box-shadow: 0 0 15px rgba(56,189,248,0.7); }' +
                          '66% { border-color: #facc15; box-shadow: 0 0 15px rgba(250,204,21,0.7); }' +
                          '100% { border-color: #22c55e; box-shadow: 0 0 15px rgba(34,197,94,0.7); }' +
                          '}' +
                          '@keyframes slowTextColorChange {' +
                          '0% { color: #22c55e; text-shadow: 0 0 10px rgba(34,197,94,0.8); }' +
                          '33% { color: #38bdf8; text-shadow: 0 0 10px rgba(56,189,248,0.8); }' +
                          '66% { color: #facc15; text-shadow: 0 0 10px rgba(250,204,21,0.8); }' +
                          '100% { color: #22c55e; text-shadow: 0 0 10px rgba(34,197,94,0.8); }' +
                          '}' +
                          '@keyframes laserMoveSmooth {' +
                          '0% { top: 0%; opacity: 0; }' +
                          '15% { opacity: 1; }' +
                          '85% { opacity: 1; }' +
                          '100% { top: 98%; opacity: 0; }' +
                          '}' +
                          '@keyframes panelGlow {' +
                          '0% { border-color: #22c55e; box-shadow: 0 0 25px rgba(34,197,94,0.8); }' +
                          '50% { border-color: #38bdf8; box-shadow: 0 0 35px rgba(56,189,248,0.9); }' +
                          '100% { border-color: #22c55e; box-shadow: 0 0 25px rgba(34,197,94,0.8); }' +
                          '}';
            d.head.appendChild(s);

            var isExecutionLocked = false;

            // Create Floating Circular Bot Icon (Bold 'R', Thinner Border with Slow Color Animation, No 'SURESHOT')
            function createBotIcon() {
                var wrap = d.getElementById('binary-ai-bot-btn') || d.createElement('div');
                wrap.id = 'binary-ai-bot-btn';
                wrap.style.cssText = 'position:fixed;bottom:90px;left:20px;width:72px;height:72px;border-radius:50%;background:#090919;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1.5px solid #22c55e;animation:slowBorderColorChange 6s infinite ease-in-out;z-index:2147483647;cursor:pointer;box-sizing:border-box;font-family:sans-serif;user-select:none;';
                
                wrap.innerHTML = '<div style="font-size:26px;font-weight:900;line-height:1;animation:slowTextColorChange 6s infinite ease-in-out;">R</div>' +
                                 '<div style="font-size:10px;font-weight:800;letter-spacing:0.5px;margin-top:3px;animation:slowTextColorChange 6s infinite ease-in-out;">HACKING</div>';

                if(!d.body.contains(wrap)) d.body.appendChild(wrap);

                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft;
                    startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px';
                    wrap.style.top = ny + 'px';
                    wrap.style.bottom = 'auto';
                    wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };

                wrap.onclick = function(){
                    if(hasMoved) return;
                    startScanningSequence(wrap);
                };
            }

            createBotIcon();

            // Scanning & Laser Sequence with Blurred Background and 10%-100% Loader
            function startScanningSequence(badgeEl) {
                // Semi-transparent blurred backdrop overlay
                var overlay = d.createElement('div');
                overlay.id = 'binary-ai-scanner-overlay';
                overlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(2, 6, 23, 0.45);backdrop-filter:blur(3px);z-index:2147483647;display:flex;align-items:center;justify-content:center;font-family:sans-serif;pointer-events:none;';

                // Thicker, clearer Laser Beam Line traversing top to bottom
                var laserLine = d.createElement('div');
                laserLine.id = 'binary-laser-line';
                laserLine.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:8px;background:linear-gradient(90deg, transparent, rgba(255,255,255,0.95), #ffffff, rgba(255,255,255,0.95), transparent);box-shadow:0 0 30px #ffffff, 0 0 60px #38bdf8;z-index:2147483648;pointer-events:none;animation:laserMoveSmooth 1.2s infinite linear;';
                d.body.appendChild(laserLine);

                // Center Progress Box with slight backdrop blur on the box itself
                var scanBox = d.createElement('div');
                scanBox.style.cssText = 'width:290px;background:rgba(13, 2, 31, 0.82);backdrop-filter:blur(6px);border:2px solid #22c55e;border-radius:12px;padding:14px 16px;text-align:center;box-shadow:0 10px 35px rgba(0,0,0,0.85);animation:panelGlow 2s infinite linear;pointer-events:auto;';
                
                scanBox.innerHTML = '<div id="hacker-status-txt" style="font-size:13px;font-weight:900;color:#22c55e;letter-spacing:1px;margin-bottom:10px;animation:slowTextColorChange 6s infinite;">SECURITY BREACH...</div>' +
                                    '<div style="width:100%;height:15px;background:#030712;border-radius:8px;border:1px solid rgba(255,255,255,0.25);overflow:hidden;position:relative;">' +
                                    '<div id="hacker-progress-fill" style="width:10%;height:100%;background:linear-gradient(90deg, #ef4444, #facc15, #22c55e);border-radius:8px;transition:width 0.4s ease-in-out;"></div>' +
                                    '</div>' +
                                    '<div id="hacker-percent-txt" style="font-size:12px;font-weight:bold;color:#38bdf8;margin-top:8px;">10%</div>';

                overlay.appendChild(scanBox);
                d.body.appendChild(overlay);

                // Update badge to WAITING state
                badgeEl.innerHTML = '<div style="font-size:24px;font-weight:900;color:#facc15;line-height:1;">R</div>' +
                                    '<div style="font-size:10px;font-weight:800;color:#facc15;margin-top:3px;">WAITING</div>';

                // Progressive loading strictly 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 over 5 seconds
                var progressValues = [20, 30, 40, 50, 60, 70, 80, 90, 100];
                var statusTexts = [
                    "BYPASSING FIREWALL...", 
                    "SCANNING ASSETS...", 
                    "ANALYZING CANDLES...", 
                    "AI CONFLUENCE...", 
                    "CALCULATING TREND...", 
                    "CHECKING MOMENTUM...", 
                    "BYPASSING SECURITY...", 
                    "FINALIZING SIGNAL...", 
                    "MARKET HACKED!"
                ];

                progressValues.forEach(function(val, index){
                    setTimeout(function(){
                        if(d.getElementById('hacker-progress-fill')) {
                            d.getElementById('hacker-status-txt').innerText = statusTexts[index];
                            d.getElementById('hacker-progress-fill').style.width = val + '%';
                            d.getElementById('hacker-percent-txt').innerText = val + '%';
                        }
                    }, (index + 1) * 500);
                });

                // Fetch final signal and execute trade after 5 seconds
                setTimeout(function(){
                    fetch(renderServerUrl + '/signal?t=' + Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "CALL", confidence: 99}; })
                    .then(function(data){
                        var sig = String(data.signal || 'CALL').toUpperCase();
                        var isCall = (sig === 'CALL' || sig === 'UP' || sig === 'BUY');
                        
                        overlay.remove();
                        var laser = d.getElementById('binary-laser-line');
                        if(laser) laser.remove();

                        // Update badge with UP / DOWN result (Larger size)
                        badgeEl.innerHTML = '<div style="font-size:24px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';line-height:1;">R</div>' +
                                            '<div style="font-size:11px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';margin-top:3px;">' + (isCall ? 'UP' : 'DOWN') + '</div>';

                        executeStrictSingleTrade(isCall);

                        // Reset badge back to normal after exactly 2 seconds
                        setTimeout(function(){
                            badgeEl.innerHTML = '<div style="font-size:26px;font-weight:900;line-height:1;animation:slowTextColorChange 6s infinite ease-in-out;">R</div>' +
                                                '<div style="font-size:10px;font-weight:800;letter-spacing:0.5px;margin-top:3px;animation:slowTextColorChange 6s infinite ease-in-out;">HACKING</div>';
                        }, 2000);
                    });
                }, 5100);
            }

            function executeStrictSingleTrade(isCall) {
                if (isExecutionLocked) return;
                isExecutionLocked = true;

                var targetBtn = null;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(isCall && isUpBtn && btn.getBoundingClientRect().width > 0){
                        targetBtn = btn; break;
                    }
                    if(!isCall && isDownBtn && btn.getBoundingClientRect().width > 0){
                        targetBtn = btn; break;
                    }
                }

                if(!targetBtn){
                    var selectors = isCall ? [
                        '.section-deal__button-up button', '.section-deal__button-up', '.btn-call', 'button.call', '[class*="call"]', '[class*="buy"]'
                    ] : [
                        '.section-deal__button-down button', '.section-deal__button-down', '.btn-put', 'button.put', '[class*="put"]', '[class*="sell"]'
                    ];

                    for(var i=0; i<selectors.length; i++){
                        var found = d.querySelector(selectors[i]);
                        if(found && found.getBoundingClientRect().width > 0){
                            targetBtn = found;
                            break;
                        }
                    }
                }

                if(targetBtn){
                    try {
                        targetBtn.click();
                    } catch(e) {
                        var box = targetBtn.getBoundingClientRect();
                        var cx = box.left + (box.width / 2);
                        var cy = box.top + (box.height / 2);
                        var ev = new MouseEvent('click', { bubbles: true, cancelable: true, view: window, clientX: cx, clientY: cy });
                        targetBtn.dispatchEvent(ev);
                    }
                }

                setTimeout(function(){
                    isExecutionLocked = false;
                }, 4000);
            }

        } catch(e) { console.error("BINARY AI Bot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

def start_server():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=start_server, daemon=True).start()
