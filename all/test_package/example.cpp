#include <small_memory_tree/small_memory_tree.hxx>
#include <st_tree.h>
int main() {
  auto tree = st_tree::tree<int>{};
  tree.insert(1);
  tree.root().insert(2);
  tree.root().insert(3);
  tree.root()[0].insert(4);
  tree.root()[0][0].insert(42);
  tree.root()[1].insert(42);
  tree.root()[1][0].insert(42);
  assert(small_memory_tree::vectorToTree(
             small_memory_tree::treeToVector(tree, 255, 254), 255, 2) == tree);
}