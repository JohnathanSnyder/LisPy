

all:
	chmod +x lispy.py

array:
	cat examples/array.lisp ; python3.3 lispy.py examples/array.lisp

dictionary:
	cat examples/dictionary.lisp ; python3.3 lispy.py examples/dictionary.lisp

conditional:
	cat examples/conditional.lisp ;  python3.3 lispy.py examples/conditional.lisp

recursion:
	cat examples/recursion.lisp ;  python3.3 lispy.py examples/recursion.lisp

functions:
	cat examples/functions.lisp ;  python3.3 lispy.py examples/functions.lisp

list:
	cat examples/list.lisp ;  python3.3 lispy.py llist.lisp
