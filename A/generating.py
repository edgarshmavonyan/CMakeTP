FILE = open("index.h", "w")
FILE.write("#include <iostream>\n")
FILE.write("void index_included() { std::cout << \"index.h is included\" << std::endl;}")
FILE.close()
