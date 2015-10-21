### Tumx hiearchy
* session:window.pane 

### Session Management.
* `tmux new -s session_name` 
* creates a new tmux session named session_name

* `tmux detach(prefix + d)`
* detach the currently attached session.

* `tmux attach -t session_name`
* attaches to an existing session session_name

* `exit`
* Close the session.


### Windows management.
* To organize better use the context name instead of random letters. For e.g. like client work or python work.

* `tmux new-window (prefix + c)`
creates a new window.

* `tmux select-window -t:0-9 (prefix + 0-9)`
* To select a window.

* `tmux rename-window (prefix + ,)`
* to rename a window.

* ` prefix + & ` => kill all windows.

### Pane management.
* `tmux split-window (prefix + “)`
* splits the window into two vertical panes

* `tmux split-window -h (prefix + %)`
* splits the window into two horizontal panes

* `tmux swap-pane -[UDLR] (prefix + { or })`
* swaps pane with another in the specified direction

* `tmux select-pane -[UDLR]`
* selects the next pane in the specified direction

* `tmux select-pane -t :.+`
* selects the next pane in numerical order

* prefix + q 
* Momentrily bring up the pane numbers.

* prefix + o
* Rotates the content the current pane and the next pane .

* `prefix + x or exit`
* Kill the current pane.

* Hold down prefix key and then press arrow to increase or decrease size.

### Special Commands
* `prefix + ?` => get the key bindings.
* Learn about the synchronization mode where you type in one and automatically does in another.


* Cheat sheet => https://gist.github.com/MohamedAlaa/2961058
