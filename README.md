# Simple Connect 4 AI
### How to Play
<p><code> python -i connectAI.py </code></p>
<p><code> board = Board() </code></p>
<p><code> player = Player(ox,tbt,ply) </code></p>
ox is the player type. ox = "O","X"  
tbt is the tiebreaker strategy. tbt = "LEFT", "RIGHT", "RANDOM"  
ply is how long the AI will look into the future. ply = "0,1,2,3,...". Higher ply means longer prcess time  

For two human players:  
<p><code> board.playGame('human','human')</code></p>

For two AI players:
<p><code> board.playGame(Player('x',"RIGHT",1),Player('o',"RANDOM",2))</code></p>

For human vs AI:  
<p><code> board.playGame('human', Player('o',"LEFT", 1))</code></p>
