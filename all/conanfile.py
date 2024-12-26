from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get
from conan.tools.cmake import CMakeToolchain


class SmallMemoryTree(ConanFile):
    name = "small_memory_tree"
    homepage = "https://github.com/werto87/small_memory_tree"
    description = "Compress sl_tree. Decompress compressed sl_tree"
    topics = ("tree", "memory")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    generators =  "CMakeDeps"
    options = {
        "with_st_tree": [True, False],
        "with_stlplus_tree": [True, False]
    }
    default_options = {
        "with_st_tree": False,
        "with_stlplus_tree": False
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False #workaround because this leads to useless options in cmake-tools configure
        tc.variables["WITH_ST_TREE"] = self.options.with_st_tree
        tc.variables["WITH_STLPLUS_TREE"] = self.options.with_stlplus_tree
        tc.generate()

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["fmt"].header_only = True

    def requirements(self):
        self.requires("boost/1.85.0")
        if self.options.with_st_tree:
            self.requires("st_tree/1.2.1")
        if self.options.with_stlplus_tree:
            self.requires("stlplus/3.16.0")            
        self.requires("confu_algorithm/1.1.1")

    def layout(self):
        cmake_layout(self, src_folder=self.name+"-"+str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.components[self.name].requires = ["boost::headers","confu_algorithm::confu_algorithm"]
        if self.options.with_st_tree:
            self.cpp_info.components[self.name].requires.append("st_tree::st_tree")
        if self.options.with_stlplus_tree:
            self.cpp_info.components[self.name].requires.append("stl_plus::stl_plus")  