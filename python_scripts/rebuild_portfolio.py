import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the entire <div class="carousel-container"> ... </div>
new_portfolio_html = """            <div class="portfolio-sticky-wrapper" id="portfolioWrapper">
                <div class="portfolio-sticky-container">
                    <div class="portfolio-track" id="portfolioTrack">
                        
                        <a href="portfolio1.html" class="portfolio-panel p1">
                            <div class="panel-content">
                                <h2 class="panel-title">UEL TERM-1</h2>
                                <div class="panel-line"></div>
                                <span class="panel-link">LEARN MORE</span>
                            </div>
                        </a>

                        <a href="portfolio2.html" class="portfolio-panel p2">
                            <div class="panel-content">
                                <h2 class="panel-title">UEL TERM-2</h2>
                                <div class="panel-line"></div>
                                <span class="panel-link">LEARN MORE</span>
                            </div>
                        </a>

                        <a href="portfolio3.html" class="portfolio-panel p3">
                            <div class="panel-content">
                                <h2 class="panel-title">TECHNICAL</h2>
                                <div class="panel-line"></div>
                                <span class="panel-link">LEARN MORE</span>
                            </div>
                        </a>

                        <a href="portfolio4.html" class="portfolio-panel p4">
                            <div class="panel-content">
                                <h2 class="panel-title">ARCHITECTURE</h2>
                                <div class="panel-line"></div>
                                <span class="panel-link">LEARN MORE</span>
                            </div>
                        </a>

                        <a href="portfolio5.html" class="portfolio-panel p5">
                            <div class="panel-content">
                                <h2 class="panel-title">CO-WORKING</h2>
                                <div class="panel-line"></div>
                                <span class="panel-link">LEARN MORE</span>
                            </div>
                        </a>

                    </div>
                </div>
            </div>"""

# Find the start and end of carousel-container
# Since we know exactly where it is, we can use regex to replace it
html = re.sub(r'<div class="carousel-container">.*?</button>\s*</div>\s*</div>', new_portfolio_html, html, flags=re.DOTALL)

# Add the script at the bottom of the body
script_js = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const wrapper = document.getElementById('portfolioWrapper');
            const track = document.getElementById('portfolioTrack');
            if (!wrapper || !track) return;

            let isInView = false;
            const observer = new IntersectionObserver((entries) => {
                isInView = entries[0].isIntersecting;
            });
            observer.observe(wrapper);

            window.addEventListener('scroll', () => {
                if (!isInView) return;
                const wrapperRect = wrapper.getBoundingClientRect();
                const wrapperTop = wrapperRect.top;
                const wrapperHeight = wrapperRect.height;
                const windowHeight = window.innerHeight;
                const scrollDistance = wrapperHeight - windowHeight;
                
                let progress = -wrapperTop / scrollDistance;
                progress = Math.max(0, Math.min(1, progress)); 

                // Track total width is 5 * 80vw + 6 * 10vw = 460vw
                // Window width is 100vw. We need to translate by -(460vw - 100vw) = -360vw
                const moveX = progress * -360; 
                track.style.transform = `translate3d(${moveX}vw, 0, 0)`;
            });
            
            let lastScrollY = window.scrollY;
            let velocity = 0;
            let tiltY = 0;
            let tiltZ = 0;

            const updateTilt = () => {
                const currentScrollY = window.scrollY;
                velocity = currentScrollY - lastScrollY;
                lastScrollY = currentScrollY;
                
                if (isInView) {
                    const targetTiltY = Math.max(-10, Math.min(10, velocity * 0.05));
                    const targetTiltZ = Math.max(-2, Math.min(2, velocity * 0.01));
                    tiltY += (targetTiltY - tiltY) * 0.1;
                    tiltZ += (targetTiltZ - tiltZ) * 0.1;
                    
                    const panels = document.querySelectorAll('.portfolio-panel');
                    panels.forEach(panel => {
                        panel.style.transform = `perspective(1200px) rotateY(${tiltY}deg) rotateZ(${tiltZ}deg)`;
                    });
                }
                
                requestAnimationFrame(updateTilt);
            };
            updateTilt();
        });
    </script>
</body>
"""
html = html.replace("</body>", script_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update style.css
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* --- NEW PORTFOLIO HORIZONTAL SCROLL --- */
.portfolio {
    padding: 0;
    overflow: hidden;
}
.portfolio .container {
    max-width: 100%;
    padding: 0;
}
.portfolio .section-header {
    padding: 100px 5% 50px;
    margin: 0;
}
.portfolio-sticky-wrapper {
    height: 400vh;
    position: relative;
    width: 100%;
}
.portfolio-sticky-container {
    position: sticky;
    top: 0;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    background-color: var(--dark);
    display: flex;
    align-items: center;
}
.portfolio-track {
    display: flex;
    align-items: center;
    height: 80vh;
    width: max-content;
    padding: 0 10vw;
    gap: 10vw;
    will-change: transform;
}
.portfolio-panel {
    width: 80vw;
    height: 70vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    overflow: hidden;
    border-radius: 4px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    will-change: transform;
}

.portfolio-panel.p1, .portfolio-panel.p2, .portfolio-panel.p3, .portfolio-panel.p4, .portfolio-panel.p5 {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.portfolio-panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.4);
    z-index: 1;
    transition: background 0.4s ease;
}
.portfolio-panel:hover::before {
    background: rgba(0,0,0,0.1);
}

.panel-content {
    position: relative;
    z-index: 2;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.panel-title {
    font-size: clamp(3rem, 8vw, 10rem);
    font-weight: 700;
    text-transform: uppercase;
    color: transparent;
    -webkit-text-stroke: 2px #fff;
    margin: 0;
    letter-spacing: 2px;
    transition: all 0.4s ease;
}

.portfolio-panel:hover .panel-title {
    color: rgba(255,255,255,0.1);
    transform: scale(1.02);
}

.panel-line {
    width: 0px;
    height: 2px;
    background-color: #fff;
    margin: 20px 0;
    transition: width 0.4s ease;
}

.portfolio-panel:hover .panel-line {
    width: 80px;
}

.panel-link {
    font-size: 1rem;
    color: #fff;
    font-weight: 600;
    letter-spacing: 4px;
    text-transform: uppercase;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.4s ease;
}

.portfolio-panel:hover .panel-link {
    opacity: 1;
    transform: translateY(0);
}
"""

css += new_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Phase 2 & 3 Portfolio Redesign complete.")
