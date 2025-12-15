# Implementing integer variable assignments
1. Get parsing going
-   get tokenization going
-   get parser going
-   generate AST tree
-   -   pretty-print to OUTPUT_PATH/ast.txt
2. Generate IR
-   desugar AST
-   generate IR
-   -   pretty-print to OUTPUT_PATH/ir.txt
3. Pass IR
-   optimize IR
-   prepare c conversion
-   -   start logging in OUTPUT_PATH/build.log
4.  emit C code
-   get required headers
-   -   stdio.h , stdlib.h , etc.
-   format IR to C
-   emit C code in OUTPUT_PATH/OUTPUT_NAME.c