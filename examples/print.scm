
(def (fact n)
  (if (= n 1)
    1
    (* n (fact (- n 1)))))

(println (fact 4))

(def a (make-dict))
(insert-dict a "a" 1)
(insert-dict a "hi" 2)
(println (get-dict a "a"))
(println (get-dict a "hi"))