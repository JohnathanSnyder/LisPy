
(def d (make-dict))

(insert-dict d "a" 0)
(insert-dict d "b" 1)
(insert-dict d "c" 2)
(insert-dict d "d" 3)
(insert-dict d "e" 4)

(println (get-dict d "a"))
(println (get-dict d "b"))
(println (get-dict d "c"))
(println (get-dict d "d"))
(println (get-dict d "e"))
