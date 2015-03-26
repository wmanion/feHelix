" Here are settings for vim 
" some of these settings may already be set by default
" placing a double quote before text makes that text a comment

set wm=8        " set wrapmargin
set nohls       " turn off highlight on search
set et          " turn on expand tab
set ruler
set backspace=2 "make it work in insert correctly if it doesn't by default

" colorscheme adjustments :hi lists the symbols and values for this
colo evening    " change the colorscheme
"colo morning    " change the colorscheme
"colo desert    " change the colorscheme

syntax on       " this is not always the default
" make the preprocessor stuff a lighter color
hi PreProc ctermfg=Yellow
hi Constant cterm=bold, ctermfg=White
"hi Constant cterm=bold,underline ctermfg=White
"hi Statement cterm=bold,underline ctermfg=Yellow

"show the line number in the left column of edit session
set number

" turn on comment continuation for C style comments
set fo-=r       " formatoptions r adds new comment line automagically
set com=s0:/*,mb:*,ex:*/        " only apply on C comments
"
" note : this feature is broken in some versions of ubuntu 
set viminfo='20,\"500
"
" AUTO-COMMANDS
" this moves the cursor to the last File mark
autocmd BufEnter * '"

"Some specific file type settings:
" for Makefiles
autocmd BufEnter ?akefile* set noet ts=8 sw=8 nocindent
" for source code
autocmd BufEnter *.cpp,*.cxx,*.h,*.c,*.java,*.pl set et ts=3 sw=4 cindent
" for grade files
autocmd BufEnter *.def set et ts=8 sw=8 wm=0 nocindent
" for html
autocmd BufEnter *.html set et ts=4 sw=4 wm=8 nocindent
"
" some abbreviations and mappings
ab teh the
ab weasle weasel
ab tomarrow tomorrow

" turn on the man page plugin
runtime ftplugin/man.vim
"
" starts a C++ program
map  o#include<iostream><CR>using namespace std;<CR>int main()<CR>{<CR>return 0;<CR>}<ESC>[[o
" creates class header
map  yypkiclass <ESC>o{<CR>private:<CR>public:<CR>};<ESC>jddkkp=$yy2pkA ( void );<ESC>jA ( const <ESC>JA & );<ESC>yypdwyypkdw$xxaoperator = <ESC>J

" starts a C program
map  o#include<stdio.h><CR>#include<stdlib.h><CR>int main()<CR>{<CR>return 0;<CR>}<ESC>[[o


set fo-=r       " formatoptions r adds new comment line automagically

" allow the mouse to work in vim
" after setting this, you will need to use: shift+right mouse to paste
" from the clipboard
set mouse=a

"sets control sequences - maps control characters to commands
map <C-G> 1G=G
map <C-P> :N!<CR><C-G>
map <C-N> :n!<CR><C-G>
map <C-M> :n!<CR>G<C-G>
"hi Comment ctermfg=darkmagenta
"hi Comment ctermbg=black
