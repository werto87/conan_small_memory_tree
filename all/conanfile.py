from conans import ConanFile, tools
from conans.tools import check_min_cppstd
import os


class SmallMemoryTree(ConanFile):
    name = "small_memory_tree"
    homepage = "https://github.com/werto87/small_memory_tree"
    description = "Compress sl_tree. Decompress compressed sl_tree"
    topics = ("tree", "memory")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("catch2/2.13.9")
        self.requires("st_tree/1.2.1")
        self.requires("range-v3/0.12.0")
        self.requires("boost/1.78.0")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        # This should lead to an Include path like #include "include_folder/IncludeFile.hxx"
        self.copy("*.h*",
                  dst="include/small_memory_tree",
                  src="source_subfolder/small_memory_tree")

    def package_id(self):
        self.info.header_only()