% Tiny Prolog companion for the logic side of the course.
% Literals are represented as pos(X) and neg(X).

complement(pos(X), neg(X)).
complement(neg(X), pos(X)).

tautology(Clause) :-
    member(Literal, Clause),
    complement(Literal, Other),
    member(Other, Clause).

remove_literal(_, [], []).
remove_literal(X, [X|Rest], Clean) :-
    remove_literal(X, Rest, Clean).
remove_literal(X, [Y|Rest], [Y|Clean]) :-
    X \= Y,
    remove_literal(X, Rest, Clean).

resolve_on(Left, Right, Literal, Resolvent) :-
    complement(Literal, Other),
    member(Literal, Left),
    member(Other, Right),
    remove_literal(Literal, Left, LeftClean),
    remove_literal(Other, Right, RightClean),
    append(LeftClean, RightClean, Resolvent).

