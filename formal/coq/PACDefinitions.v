Require Import Coq.Lists.List.
Require Import Coq.Bool.Bool.

Import ListNotations.

Definition example := nat.
Definition hypothesis := example -> bool.

Fixpoint agrees_on (h1 h2 : hypothesis) (xs : list example) : bool :=
  match xs with
  | [] => true
  | x :: rest => Bool.eqb (h1 x) (h2 x) && agrees_on h1 h2 rest
  end.

Theorem agrees_on_refl :
  forall (h : hypothesis) (xs : list example), agrees_on h h xs = true.
Proof.
  intros h xs.
  induction xs as [|x rest IH].
  - reflexivity.
  - simpl. destruct (h x); simpl; exact IH.
Qed.
