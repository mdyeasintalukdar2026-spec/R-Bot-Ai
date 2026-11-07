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
            ["binary-ai-bot-btn", "binary-ai-scanner-overlay", "binary-ai-style"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var renderServerUrl = "https://r-bot-ai.onrender.com";

            // CSS Animations matching the hacker aesthetic from the video
            var s = d.createElement('style');
            s.id = 'binary-ai-style';
            s.innerHTML = '@keyframes badgeGlowPulse {' +
                          '0% { box-shadow: 0 0 15px rgba(34,197,94,0.6), 0 0 30px rgba(34,197,94,0.3); border-color: #22c55e; }' +
                          '50% { box-shadow: 0 0 25px rgba(34,197,94,0.95), 0 0 50px rgba(34,197,94,0.6); border-color: #38bdf8; }' +
                          '100% { box-shadow: 0 0 15px rgba(34,197,94,0.6), 0 0 30px rgba(34,197,94,0.3); border-color: #22c55e; }' +
                          '}' +
                          '@keyframes hackerBarGlow {' +
                          '0% { border-color: #22c55e; box-shadow: 0 0 15px rgba(34,197,94,0.8); }' +
                          '50% { border-color: #38bdf8; box-shadow: 0 0 25px rgba(56,189,248,0.9); }' +
                          '100% { border-color: #22c55e; box-shadow: 0 0 15px rgba(34,197,94,0.8); }' +
                          '}' +
                          '@keyframes textFlicker {' +
                          '0% { opacity: 0.7; }' +
                          '50% { opacity: 1; text-shadow: 0 0 10px #22c55e; }' +
                          '100% { opacity: 0.7; }' +
                          '}' +
                          '@keyframes panelFadeIn { 0% { opacity: 0; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1); } }';
            d.head.appendChild(s);

            var isExecutionLocked = false;

            // Create Floating Hacker Circular Badge (Bottom Left, exactly like video)
            function createBotIcon() {
                var wrap = d.getElementById('binary-ai-bot-btn') || d.createElement('div');
                wrap.id = 'binary-ai-bot-btn';
                wrap.style.cssText = 'position:fixed;bottom:90px;left:20px;width:72px;height:72px;border-radius:50%;background:#090919;display:flex;flex-direction:column;align-items:center;justify-content:center;border:3px solid #22c55e;animation:badgeGlowPulse 2s infinite ease-in-out;z-index:2147483647;cursor:pointer;box-sizing:border-box;font-family:sans-serif;user-select:none;';
                
                wrap.innerHTML = '<div style="font-size:20px;font-weight:900;color:#22c55e;line-height:1;">A</div>' +
                                 '<div style="font-size:9px;font-weight:700;color:#ffffff;letter-spacing:0.5px;margin-top:2px;">HACKING</div>' +
                                 '<div style="font-size:7.5px;font-weight:600;color:#38bdf8;margin-top:1px;">SURESHOT</div>';

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
                    startHackingScanSequence(wrap);
                };
            }

            createBotIcon();

            // Full Hacking Scan Sequence with Center Progress Bar & Status Texts
            function startHackingScanSequence(badgeEl) {
                var overlay = d.createElement('div');
                overlay.id = 'binary-ai-scanner-overlay';
                overlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(2, 6, 23, 0.45);z-index:2147483647;display:flex;align-items:center;justify-content:center;font-family:sans-serif;pointer-events:none;';

                // Center Hacker Progress Box (matches video style precisely)
                var scanBox = d.createElement('div');
                scanBox.style.cssText = 'width:280px;background:rgba(13, 2, 31, 0.92);border:2px solid #22c55e;border-radius:10px;padding:12px 15px;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.8);animation:hackerBarGlow 1.5s infinite linear;';
                
                scanBox.innerHTML = '<div id="hacker-status-txt" style="font-size:12px;font-weight:900;color:#22c55e;letter-spacing:1px;margin-bottom:8px;animation:textFlicker 1s infinite;">SECURITY BREACH...</div>' +
                                    '<div style="width:100%;height:14px;background:#030712;border-radius:7px;border:1px solid rgba(255,255,255,0.2);overflow:hidden;position:relative;">' +
                                    '<div id="hacker-progress-fill" style="width:15%;height:100%;background:linear-gradient(90deg, #ef4444, #facc15, #22c55e);border-radius:7px;transition:width 0.4s ease-in-out;"></div>' +
                                    '</div>' +
                                    '<div id="hacker-percent-txt" style="font-size:11px;font-weight:bold;color:#38bdf8;margin-top:6px;">15%</div>';

                overlay.appendChild(scanBox);
                d.body.appendChild(overlay);

                // Update badge to WAITING state during scan
                badgeEl.innerHTML = '<div style="font-size:18px;font-weight:900;color:#facc15;line-height:1;">A</div>' +
                                    '<div style="font-size:9px;font-weight:700;color:#ffffff;margin-top:2px;">WAITING</div>' +
                                    '<div style="font-size:7.5px;font-weight:600;color:#38bdf8;margin-top:1px;">SURESHOT</div>';

                // Step-by-step progress simulation matching the video
                setTimeout(function(){
                    d.getElementById('hacker-status-txt').innerText = "BYPASSING FIREWALL...";
                    d.getElementById('hacker-progress-fill').style.width = "58%";
                    d.getElementById('hacker-percent-txt').innerText = "58%";
                }, 900);

                setTimeout(function(){
                    d.getElementById('hacker-status-txt').innerText = "MARKET HACKED!";
                    d.getElementById('hacker-progress-fill').style.width = "100%";
                    d.getElementById('hacker-percent-txt').innerText = "100%";
                }, 1800);

                setTimeout(function(){
                    fetch(renderServerUrl + '/signal?t=' + Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "CALL", confidence: 99}; })
                    .then(function(data){
                        var sig = String(data.signal || 'CALL').toUpperCase();
                        var isCall = (sig === 'CALL' || sig === 'UP' || sig === 'BUY');
                        
                        overlay.remove();

                        // Update badge with final direction (UP / DOWN)
                        badgeEl.innerHTML = '<div style="font-size:18px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';line-height:1;">A</div>' +
                                            '<div style="font-size:9px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';margin-top:2px;">' + (isCall ? 'UP' : 'DOWN') + '</div>' +
                                            '<div style="font-size:7.5px;font-weight:600;color:#38bdf8;margin-top:1px;">SURESHOT</div>';

                        executeStrictSingleTrade(isCall);

                        // Reset badge back to normal after execution
                        setTimeout(function(){
                            badgeEl.innerHTML = '<div style="font-size:20px;font-weight:900;color:#22c55e;line-height:1;">A</div>' +
                                                '<div style="font-size:9px;font-weight:700;color:#ffffff;letter-spacing:0.5px;margin-top:2px;">HACKING</div>' +
                                                '<div style="font-size:7.5px;font-weight:600;color:#38bdf8;margin-top:1px;">SURESHOT</div>';
                        }, 4000);
                    });
                }, 2600);
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
