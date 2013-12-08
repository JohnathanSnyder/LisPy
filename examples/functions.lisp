
(def a (list 1 2 3 4 5 6 7 8 9))

(def (square x) (* x x))

(println "List without being mapped")
(println a)
(println "")

(println "List that is maped with square function")
(println (map square a))
