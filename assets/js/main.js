// 手機選單開合
(function () {
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileMenu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      menu.classList.toggle("open");
    });
    // 點選連結後收起選單
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.classList.remove("open");
      });
    });
  }

  // 依目前檔名高亮導航
  var path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav a, .mobile-menu a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path) a.classList.add("active");
  });
})();
