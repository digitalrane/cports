pkgname = "kgamma"
pkgver = "6.1.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE tool for adjusting monitor gamma"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kgamma"
source = f"$(KDE_SITE)/plasma/{pkgver}/kgamma-{pkgver}.tar.xz"
sha256 = "2f43ec6b4abac27249b101594f19f222fe7e5947054f5252c11a9d9ec20ab42c"
hardening = ["vis"]