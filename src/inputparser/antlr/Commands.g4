grammar Commands ;

// PARSER RULES
prog        : terminal ('\n' | EOF);

// combine commands with ';'
terminal    : WHITESPACE? combine*? instuctions WHITESPACE?;
combine     : instuctions WHITESPACE? ';' WHITESPACE? ;

// pipe commands into each other
instuctions : WHITESPACE? (pipe)* command WHITESPACE? ;
pipe        : command WHITESPACE? '|' WHITESPACE? ;

// simple command structure
command
: WHITESPACE? app args? (WHITESPACE redir_in)? (WHITESPACE redir_out)? WHITESPACE?
;
// app name
app         : atom ;
// arguments
args        : (WHITESPACE? flag (WHITESPACE? arg+)? WHITESPACE?)+ | arg+;
arg         : (WHITESPACE (atom | globbed)) ;
flag        : '-' atom  | '--' atom;

// redirection
redir_in    : '<' WHITESPACE? atom ;
redir_out   : '>' WHITESPACE? atom ;

// globbing support
globbed     : '*' ;

// quoting support
atom
: WORD
| QUOTEDTEXT
| atom substituted atom?
| substituted atom?
| atom globbed atom?
| globbed atom?
;

//command substitution
substituted : '`' terminal '`' ;

// LEXER RULES

fragment LOWER          : [a-z] ;
fragment UPPER          : [A-Z] ;
fragment NUMBER         : [0-9] ;
fragment STARTPUNCT     : ('.' | ',' | '/' | '\\') ;
fragment FULLCHAR       : ALPHANUM | '-' | '_' ;
fragment ALPHANUM       : (LOWER | UPPER | NUMBER | STARTPUNCT) ;

fragment SINGLEQUOTEWORD: ~('\r' | '\n' | '\'')* ;
fragment DOUBLEQUOTEWORD: ~('\r' | '\n' | '"')* ;

WORD                    : ALPHANUM FULLCHAR*;
WHITESPACE              : (' ' | '\t') + ;



QUOTEDTEXT
: '"' (WORD | WHITESPACE) * '"'
| '\'' (WORD | WHITESPACE) * '\''
;

OTHER                   : .+?;