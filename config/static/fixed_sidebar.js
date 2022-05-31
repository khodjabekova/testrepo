setTimeout(() => {
    const navLinkActive = document.querySelector('.sidebar .nav-item .nav-link.active')
    const sidebar = document.querySelector('.main-sidebar .sidebar')
    sidebar.scrollTo({
        top: navLinkActive.getBoundingClientRect().y - 200,
    })
}, 10)
