// Portfolio Data Structure
const portfolioPages = [
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026683/1_w0mqdj.jpg", alt: "Portfolio Page 1" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026684/2_ysuswv.jpg", alt: "Portfolio Page 2" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026684/3_sxa8i3.jpg", alt: "Portfolio Page 3" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026685/4_gye9hl.jpg", alt: "Portfolio Page 4" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026685/5_hqgpud.jpg", alt: "Portfolio Page 5" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026686/6_fkkj2a.jpg", alt: "Portfolio Page 6" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026687/7_gqene4.jpg", alt: "Portfolio Page 7" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026687/8_oqitii.jpg", alt: "Portfolio Page 8" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026887/9_1_q9mgmt.jpg", alt: "Portfolio Page 9" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026688/10_div1wj.jpg", alt: "Portfolio Page 10" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026689/11_cys56y.jpg", alt: "Portfolio Page 11" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026690/12_rzglbx.jpg", alt: "Portfolio Page 12" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026690/13_arxn5k.jpg", alt: "Portfolio Page 13" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026691/14_carxij.jpg", alt: "Portfolio Page 14" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026691/15_gur6ar.jpg", alt: "Portfolio Page 15" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026691/16_bzgrds.jpg", alt: "Portfolio Page 16" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026692/17_ypesg1.jpg", alt: "Portfolio Page 17" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026693/18_zjv04a.jpg", alt: "Portfolio Page 18" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026693/19_f5thx1.jpg", alt: "Portfolio Page 19" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026694/20_semxwm.jpg", alt: "Portfolio Page 20" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026694/21_zk01cp.jpg", alt: "Portfolio Page 21" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026695/22_kjt2sp.jpg", alt: "Portfolio Page 22" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026695/23_zlkwvu.jpg", alt: "Portfolio Page 23" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026696/24_tgglso.jpg", alt: "Portfolio Page 24" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026697/25_x0czce.jpg", alt: "Portfolio Page 25" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026697/26_gtt5p2.jpg", alt: "Portfolio Page 26" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026698/27_gdefyw.jpg", alt: "Portfolio Page 27" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026698/28_yuhrtg.jpg", alt: "Portfolio Page 28" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026699/29_hiyi88.jpg", alt: "Portfolio Page 29" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026699/30_ukv6bs.jpg", alt: "Portfolio Page 30" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026700/31_furaqq.jpg", alt: "Portfolio Page 31" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026700/32_nekx3h.jpg", alt: "Portfolio Page 32" },
    { src: "https://res.cloudinary.com/dfduodbpa/image/upload/v1784026701/33_daupez.jpg", alt: "Portfolio Page 33" },
    { src: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=", alt: "Blank Page" }
];

document.addEventListener('DOMContentLoaded', () => {
    const bookContainer = document.getElementById('book-container');
    const hardcoverFront = document.getElementById('hardcover-front');
    const coverOutside = document.getElementById('cover-outside');
    const flipBookEl = document.getElementById('flip-book');
    const innerFrame = document.getElementById('inner-pages-frame');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const pageCounter = document.querySelector('.page-counter');

    // --- 1. Cover outside = Portfolio cover, inside = SANSKRUTI info ---
    const coverImg = portfolioPages[0];
    coverOutside.innerHTML = `<img src="${coverImg.src}" alt="${coverImg.alt}" draggable="false">`;
    const sanskrutiImg = portfolioPages[1];
    document.querySelector('.hc-inside').innerHTML = `<img src="${sanskrutiImg.src}" alt="${sanskrutiImg.alt}" draggable="false">`;

    // --- 2. Inner pages start from CONTENTS (index 2) ---
    const innerPages = portfolioPages.slice(2);
    innerPages.forEach((pageObj) => {
        const pageDiv = document.createElement('div');
        pageDiv.className = 'page';
        pageDiv.innerHTML = `
            <div class="page-content">
                <img src="${pageObj.src}" alt="${pageObj.alt}" draggable="false" style="pointer-events: none;">
            </div>
        `;
        flipBookEl.appendChild(pageDiv);
    });

    // --- 3. Initialize St.PageFlip ONCE immediately ---
    // The inner-pages-frame uses visibility:hidden (not display:none) so it has layout dimensions
    const pageFlip = new St.PageFlip(flipBookEl, {
        width: 707,
        height: 500,
        size: 'stretch',
        minWidth: 300,
        maxWidth: 1000,
        minHeight: 200,
        maxHeight: 800,
        showCover: true,
        mobileScrollSupport: true,
        useMouseEvents: true,
        flippingTime: 500,
        drawShadow: true,
        maxShadowOpacity: 0.15,
        startPage: 0,
        showPageCorners: true
    });

    pageFlip.loadFromHTML(document.querySelectorAll('.page'));
    window.pageFlip = pageFlip;

    pageFlip.on('flip', (e) => {
        const cp = e.data;
        const p1 = cp + 1;
        const p2 = cp + 2;
        if (p2 <= innerPages.length) {
            pageCounter.textContent = `Pages ${p1}-${p2} / ${innerPages.length}`;
        } else {
            pageCounter.textContent = `Page ${p1} / ${innerPages.length}`;
        }
        prevBtn.disabled = false;
        nextBtn.disabled = cp >= innerPages.length - 1;
    });

    // --- 4. Open / Close logic ---
    let isOpen = false;

    hardcoverFront.addEventListener('click', () => {
        if (!isOpen) openBook();
    });

    function openBook() {
        isOpen = true;
        bookContainer.classList.remove('is-closed');
        bookContainer.classList.add('is-open');
        pageCounter.textContent = 'Pages 1-2 / ' + innerPages.length;
        prevBtn.disabled = false;
        nextBtn.disabled = false;

        // After cover animation finishes, tell St.PageFlip to recalculate
        setTimeout(() => {
            pageFlip.update();
        }, 850);
    }

    function closeBook() {
        isOpen = false;
        bookContainer.classList.remove('is-open');
        bookContainer.classList.add('is-closed');
        pageCounter.textContent = 'Cover';
        prevBtn.disabled = true;
        // Reset inner pages to first spread
        pageFlip.flip(0);
    }

    // --- 5. Nav buttons ---
    prevBtn.addEventListener('click', () => {
        if (!isOpen) return;
        const cp = pageFlip.getCurrentPageIndex();
        if (cp === 0) {
            closeBook();
        } else {
            pageFlip.flipPrev();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (!isOpen) { openBook(); return; }
        pageFlip.flipNext();
    });

    // --- 6. Keyboard ---
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            if (!isOpen) { openBook(); return; }
            pageFlip.flipNext();
        } else if (e.key === 'ArrowLeft') {
            if (!isOpen) return;
            const cp = pageFlip.getCurrentPageIndex();
            if (cp === 0) closeBook();
            else pageFlip.flipPrev();
        }
    });

    // Initial state
    prevBtn.disabled = true;
});
