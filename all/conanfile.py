from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
from conan.tools.microsoft import is_msvc
from conan.tools.scm import Version
import os


class SmallMemoryTree(ConanFile):
    name = "small_memory_tree"
    homepage = "https://github.com/werto87/small_memory_tree"
    description = "Compress sl_tree. Decompress compressed sl_tree"
    topics = ("tree", "memory")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True
    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True
        self.options["fmt"].header_only = True

    def requirements(self):
        self.requires("boost/1.84.0")
        self.requires("st_tree/1.2.1")
        self.requires("confu_algorithm/0.0.1")

    def package(self):
        copy(self, "*.h*", src=os.path.join(self.source_folder, self.name),
             dst=os.path.join(self.package_folder, "include", self.name))

