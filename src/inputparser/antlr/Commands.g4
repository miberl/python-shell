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
: WORD
| atom substituted atom?
| substituted atom?
| atom globbed atom?
| globbed atom?
| WORD? quoted_text WORD?
;

//command substitution
substituted : '`' terminal '`' ;

// quoted text
quoted_text : SINGLEQUOTE WHITESPACE? (WORD WHITESPACE?)* WHITESPACE? SINGLEQUOTE | DOUBLEQUOTE WHITESPACE? (WORD WHITESPACE?)* WHITESPACE? DOUBLEQUOTE ;

// LEXER RULES

fragment LOWER          : [a-z] ;
fragment UPPER          : [A-Z] ;
fragment NUMBER         : [0-9] ;
fragment PUNCT     : ('.' | ',' | '/' | '\\' | '_'| '-') ;
fragment ALPHANUM       : (LOWER | UPPER | NUMBER | PUNCT ) ;

WORD                    : ALPHANUM+;
WHITESPACE              : (' ' | '\t') + ;

SINGLEQUOTE : '\'' ;
DOUBLEQUOTE : '"' ;

SINGLEQUOTECHAR: ~('\r' | '\n' | '\'') ;
DOUBLEQUOTECHAR: ~('\r' | '\n' | '"') ;

OTHER                   : .+?;
