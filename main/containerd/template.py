pkgname = "containerd"
pkgver = "1.7.22"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "all",
    "man",
    f"REVISION=chimera-r{pkgrel}",
    f"VERSION={pkgver}",
]
make_install_args = ["install-man"]
make_check_target = "test"
make_check_args = ["TESTFLAGS_RACE="]
hostmakedepends = [
    "go",
    "go-md2man",
]
makedepends = [
    "libbtrfs-devel",
    "libseccomp-devel",
    "linux-headers",
]
depends = [
    "cni-plugins",
    "oci-runtime",
]
pkgdesc = "Industry-standard container runtime"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/containerd/containerd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8c5edde741b7596af63c021429a1212bd616350ed65a7b741eeffc47e27ee9a9"
# can't run tests inside namespaces
options = ["!check"]


if self.profile().arch == "riscv64":
    broken = "cgo runtime stuff"


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_file(self.files_path / "config.toml", "etc/containerd")
    self.install_service(self.files_path / "containerd")


@subpackage("containerd-stress")
def _(self):
    self.pkgdesc = "Containerd benchmarking utility"

    return ["usr/bin/containerd-stress"]


@subpackage("containerd-ctr")
def _(self):
    self.pkgdesc = "Debug / admin client for containerd"

    return ["usr/bin/ctr"]