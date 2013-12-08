
(define (fib n)
	(cond ((= n 0) 0)
				((= n 1) 1)
				(else (+ (fib (- n 1)) (fib (- n 2))))))

(define (fact n)
	(if (= n 1)
		1
		(* n (fact (- n 1)))))
