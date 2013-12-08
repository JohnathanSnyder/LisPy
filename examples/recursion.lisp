

(def (fact n)
  (if (= n 1)
    1
    (* n (fact (- n 1)))))

(println "Recursive factorial")
(print "(fact 13) ")
(println (fact 13))

