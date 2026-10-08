// The right-hand table of contents is generated from the page headings, so the
// "TACTIC Forum" entry only scrolls to its section.  Point it at the discussions.
document.addEventListener("DOMContentLoaded", function () {
    var url = "https://github.com/magic-lantern-workbench/TACTIC-Docs/discussions";
    document.querySelectorAll('.md-nav--secondary a[href="#tactic-forum"]').forEach(function (a) {
        a.setAttribute("href", url);
    });
});
