##### Complex search:
~~Search for restaurants near me with good seafood that will fit a $30 budget~~

Search for PHP· programs near Lexington that you think are autism friendly and are likely to let me use my laptop

##### Search network:
- PHP· programs near Lexington
- PHP· programs allowing computer use
- autism-friendly PHP· programs

##### Steps:
- Compile results to set:
	- Gather top results into a list
	- Remove duplicate entries
- Sort by distance to Lexington:
	- Compute distance
	- Match location to distance
	- Sort
- Sort by predicted computer use:
	- Compute prediction:
		- Search for program's policies
		- Summarize
		- Assign score 0-5
	- Match location to prediction
	- Sort
- Sort by autism-friendliness:
	- Compute prediction:
		- Reuse policy search
		- Summarize
		- Assign score 0-5
	- Match location to prediction
	- Sort

##### Thoughts

The beauty is that each step, even decomposition, is doable by an LLM·, so long as you let it take multiple generations. Just stop asking them to do everything at once and stop asking them to keep all their memories in the same place!

##### Discussion link

https://chatgpt.com/share/6744fdce-2ce8-8004-a3ce-0e8013417f36
