

(def (println s) (print s "\n"))

(def else #t)

(def nil (list))


(def (even? x) (= (mod x 2) 0))

(def (cadr x) (car (cdr x)))
(def (cddr x) (cdr (cdr x)))

(def (map proc items)
  (if (null? items)
    nil
    (cons (proc (car items)) (map proc (cdr items)))))

(def (filter p? items)
  (cond ((null? items) nil)
        ((p? (car items)) (cons (car items)
                                (filter p? (cdr items))))
        (else (filter p? (cdr items)))))

