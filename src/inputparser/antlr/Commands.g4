grammar Commands ;

// PARSER RULES
prog        : terminal? WHITESPACE? ('\n' | EOF);

// combine commands with ';'
terminal    : WHITESPACE? (instruction WHITESPACE? ';' WHITESPACE?)* instruction WHITESPACE?;

// pipe commands into each other
instruction : WHITESPACE? command (WHITESPACE? '|' WHITESPACE? command)* WHITESPACE? ;

// simple command structure
command
:  (redir_in | redir_out | WHITESPACE)* arg (WHITESPACE arg | redir_in | redir_out | WHITESPACE)*
;
// arguments
arg         : (atom | globbed) ;

// redirection
redir_in    : '<' WHITESPACE? atom ;
redir_out   : '>' WHITESPACE? atom ;

// globbing support
globbed     : '*' ;

// quoting support
atom
: (WORD | substituted | globbed | quoted_text)+
;

//command substitution
substituted : '`' terminal '`' ;

// Quoting Support
quoted_text:
(SINGLEQUOTE (DOUBLEQUOTE | '*' | '|' | ';' | '<' | '>' | QUOTEWORD | WORD | substituted | WHITESPACE)* SINGLEQUOTE)
| (DOUBLEQUOTE (SINGLEQUOTE | ';' | '*' | ';' | '*' | '<' | '>' |QUOTEWORD | WORD | substituted | WHITESPACE)* DOUBLEQUOTE)
;


// LEXER RULES

fragment LOWER          : [a-z] ;
fragment UPPER          : [A-Z] ;
fragment NUMBER         : [0-9] ;
fragment PUNCT          : ('.' | ',' | '/' | '\\' | '_'| '-') ;
fragment ALPHANUM       : (LOWER | UPPER | NUMBER | PUNCT ) ;

WORD                    : ALPHANUM+;
WHITESPACE              : (' ' | '\t') + ;

SINGLEQUOTE: '\'' ;
DOUBLEQUOTE: '"' ;
QUOTEWORD: ~('\r' | '\n' | '\'' | '"' | '`' | ' ' | '\t' | '*' | '|' | ';' | '<' | '>')+;

OTHER                   : .+?;
