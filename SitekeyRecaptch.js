(function () {
    const keysFound = new Set();
  
    // --- 1. Check for reCAPTCHA v2 --- 
    // Look for elements with a data-sitekey attribute (e.g., <div class="g-recaptcha" data-sitekey="..."></div>)
    const v2Elements = document.querySelectorAll('[data-sitekey]');
    v2Elements.forEach(el => {
      const key = el.getAttribute('data-sitekey');
      if (key) {
        keysFound.add(key);
        console.log('Found reCAPTCHA v2 site key:', key);
      }
    });
  
    // --- 2. Check for reCAPTCHA v3 in script tags ---
    // Look for script tags with a src that includes "recaptcha/api.js"
    const scriptElements = document.querySelectorAll('script[src]');
    scriptElements.forEach(script => {
      const src = script.getAttribute('src');
      if (src && src.includes('recaptcha/api.js')) {
        try {
          const url = new URL(src, location.href);
          const key = url.searchParams.get('render');
          if (key) {
            keysFound.add(key);
            console.log('Found reCAPTCHA v3 site key from script src:', key);
          }
        } catch (e) {
          // If URL parsing fails, skip this script
        }
      }
    });
  
    // --- 3. Check inline code for recaptcha.execute calls ---
    // Some pages use inline JS that calls grecaptcha.execute('SITE_KEY', ...)
    const inlineRegex = /grecaptcha\.execute\s*\(\s*['"]([^'"]+)['"]/g;
    const htmlContent = document.documentElement.innerHTML;
    let match;
    while ((match = inlineRegex.exec(htmlContent)) !== null) {
      const key = match[1];
      if (key) {
        keysFound.add(key);
        console.log('Found site key in a grecaptcha.execute call:', key);
      }
    }
  
    if (keysFound.size === 0) {
      console.log("No reCAPTCHA site keys found on this page.");
    } else {
      console.log("Done. Total keys found:", Array.from(keysFound));
    }
  })();
  