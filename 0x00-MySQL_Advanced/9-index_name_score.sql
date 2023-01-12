-- Creates an index idx_name_first_score on table names and first letter of name and score
-- Only first letter of name AND score must be indexed

CREATE INDEX idx_name_first_score
ON names(name(1), score);
