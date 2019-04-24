using Base.Threads

function sieve_erat(n)
    primes = ones(Bool, n)
    for i in 2:Int(floor(sqrt(n)))
        if primes[i] == true
            for j in i^2:i:n
                primes[j] = false
            end
        end
    end

    result = []
    for i in 2:length(primes)
        if primes[i] == true
            push!(result, i)
        end
    end
    return result
end

function fastExp(a, b, c)::BigInt
    result = 1
    exp = b
    fact = a
    while exp > 0
        if exp & 1 == 1
            result = (result * fact) % c
        end
        exp = exp ÷ 2
        fact = (fact * fact) % c
    end
    return result
end

function fpt(p)
    if p == 2
        return true
    end
    result = true
    nums = sieve_erat(p - 1)
    for a in nums
        if fastExp(a, p - 1, p) != 1
            result = false
        end
    end
    return result
end