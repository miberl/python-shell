grammar Commands ;

// PARSER RULES
prog        : terminal ('\n' | EOF);

// combine commands with ';'
terminal    : WHITESPACE? (instruction WHITESPACE? ';' WHITESPACE?)? instruction WHITESPACE?;

// pipe commands into each other
instruction : WHITESPACE? command (WHITESPACE? '|' WHITESPACE? command)* WHITESPACE? ;

// simple command structure
command
: WHITESPACE? app arg* (WHITESPACE redir_in)? (WHITESPACE redir_out)? WHITESPACE?
;
// app name
app         : atom ;
// arguments
arg         : (WHITESPACE (atom | globbed)) ;

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
(SINGLEQUOTE (DOUBLEQUOTE | '*' | '|' | ';' |QUOTEWORD | WORD | substituted | WHITESPACE)* SINGLEQUOTE)
| (DOUBLEQUOTE (SINGLEQUOTE | ';' | '*' | ';' | '*' |QUOTEWORD | WORD | substituted | WHITESPACE)* DOUBLEQUOTE)
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
QUOTEWORD: ~('\r' | '\n' | '\'' | '"' | '`' | ' ' | '\t' | '*' | '|' | ';')+;

OTHER                   : .+?;
