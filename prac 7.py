% --- FACTS ---
parent(john, mary).
parent(mary, alice).
parent(john, mike).
parent(mike, sam).

male(john).
male(mike).
male(sam).

female(mary).
female(alice).

% --- RULES ---
% father rule
father(X, Y) :-
    parent(X, Y),
    male(X).

% mother rule
mother(X, Y) :-
    parent(X, Y),
    female(X).

% grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% ancestor rule (recursive)
ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
