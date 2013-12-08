

(def (pair-cons a b)
  (lambda (x)
    (if (= x 0)
      a
      b)))

(def (pair-car x)
  (x 0))

(def (pair-cdr x)
  (x 1))

(def (create) nil)

(def (addToFront items x)
  (pair-cons x items))

(def (addToBack items x)
  (if (null? items)
    (pair-cons x nil)
    (pair-cons (pair-car items) (addToBack (pair-cdr items) x))))

(def (addAtIndex items index x)
  (if (= index 0)
    (pair-cons x items)
    (pair-cons (pair-car items) (addAtIndex (pair-cdr items) (- index 1) x))))

(def (removeFromFront items)
  (pair-cdr items))

(def (removeFromBack items)
  (if (null? (pair-cdr items))
    nil
    (pair-cons (pair-car items) (addToBack (pair-cdr items)))))

(def (removeAtIndex items index)
  (if (= index 0)
    (pair-cdr items)
    (pair-cons (pair-car items) (removeAtIndex (pair-cdr items) (- index 1)))))

(def (begin x y) y)

(def (visualize items)
 (if (null? items)
   nil
   (begin (println (pair-car items)) (visualize (pair-cdr items)))))

(def i (create))

(def i (addToFront i 5))
(def i (addToBack i 6))
(def i (addToBack i 7))
(def i (addToBack i 8))
(def i (addToBack i 9))
(def i (addToBack i 10))

(visualize i)
(println "")

(def i (addToFront i 4))
(def i (addToFront i 3))
(def i (addToFront i 2))
(def i (addToFront i 1))

(visualize i)
(println "")

(def i (addAtIndex i 4 2432))

(visualize i)
(println "")

(def i (removeAtIndex i 4))

(visualize i)
(println "")
