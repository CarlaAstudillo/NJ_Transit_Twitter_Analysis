# NJ TRANSIT TWITTER ANALYSIS
In the absence of more detailed day-to-day NJ Transit data, NJ Advance Media scraped all tweets from seven individual line twitter accounts ([@NJTRANSIT_NEC](https://twitter.com/NJTRANSIT_NEC), [@NJTRANSIT_NJCL](https://twitter.com/NJTRANSIT_NJCL), [@NJTRANSIT_ME](https://twitter.com/NJTRANSIT_ME), [@NJTRANSIT_RVL](https://twitter.com/NJTRANSIT_RVL), [@NJTRANSIT_MBPJ](https://twitter.com/NJTRANSIT_MBPJ), [@NJTRANSIT_PVL](https://twitter.com/NJTRANSIT_PVL), [@NJTRANSIT_MOBO](https://twitter.com/NJTRANSIT_MOBO)) run by NJ Transit and analyzed the last few months of delays. The Atlantic City Rail Line was excluded from the analysis because the rail does not connect to either New York Penn Station or Hoboken. In addition, the main [@NJTransit](https://twitter.com/njtransit) twitter account is not included in the analysis because much of information is then repeated in the individual NJ Transit line twitter accounts.
 
Note that this isn’t a comprehensive look at how many trains were delayed and the exact times the delays took place. This only captures what delays the NJ Transit twitter accounts decided to tweet about to alert customers. It’s an unscientific snapshot of the day-to-day experience NJ Transit customers have gone through the last few months.
 
For the whole duration of the NJ Transit summer of hell, we plan on scraping and analyzing the tweets.
 
### METHODOLOGY
 
The tweets were first scraped from the official NJ Transit twitter accounts using Python. We then filtered them out in a Jupyter notebook. Using Regex, we took out:
 
* All retweets
* All tweets referring to the same delay for the same train. This was done by removing all tweets with the word UPDATE so that only the initial delay tweet is counted
* All tweets alluding to trains operation on or close to a normal schedule
* All promotional or campaign tweets
* All tweets about other train lines that are not NJ Transit, like PATH and Metro North. We also took out mentions of the Princeton shuttle and the Newark Airport Air Train.
* All tweets that were corrections on an earlier tweet by removing all tweets with the word CORRECTION
 
We made sure we kept we only kept tweets that at least included one of these words:
 
* delays, delay, delayed
* cancelled
* Suspend, suspended
* late 
* stopped in the station
 
We then manually took out any tweets when an NJ Transit twitter account for one NJ Transit train line tweeted about a delay on a train from another train line. Finally, we stitched together all of the tweets for every line into one big dataset. 

### CATEGORIZATION
 
We also manually categorized each tweet according to who/what NJ Transit blamed the delay on in the tweet. The categories and criteria are the following:

| Category   |      Criteria      | 
|----------|-------------|
| Amtrak ALL |  All tweets that place the blame on Amtrak.|
| NJT ALL |  All tweets that don't blame Amtrak or any weather, medical or police emergency are categorized as NJ Transit related.|
| Misc ALL |  All tweets that blame miscellaneous events that have nothing to do with Amtrak or NJ Transit issues. Examples include police/fire activity, medical emergency or severe weather. |
| Amtrak derailed train |  All tweets that blame delay on an Amtrak train derailing. |
| Amtrak disabled train |  All tweets that blame delay on a disabled Amtrak train. |
| Amtrak late train |  All tweets that blame delay on a delayed or late Amtrak train ahead or if there is heavy congestion. Also includes trains that need to make additional stops or if there's a delayed connection. |
| Amtrak maintenance |  All tweets that blame delay on any programmed maintenance and track maintenance work done by Amtrak. This work happens in Northeast Corridor line, especially near NY Penn Station so it might effect other train lines. We only included tweets from other non-NEC train lines if they explicitly said that it was Amtrak work that is causing delay. |
| Amtrak problem |  All tweets that blame delay on an Amtrak switch/signal/mechanical/operational problem. |
| Amtrak speed limit |  All tweets that blame delay on the speed restrictions placed by Amtrak after derailment. |
| Medical emergency |  All tweets that blame delay on medical emergencies or sick passengers. |
| NJT derailed train |  All tweets that blame delay on a derailed NJ Transit train. |
| NJT disabled train |  All tweets that blame delay on a disabled NJ Transit train. |
| NJT equipment issue |  All tweets that blame delay on an equipment issue, which can include a break down or not enough equipment being available. |
| NJT late train |  All tweets that blame a delayed or late NJ Transit train ahead or if there is heavy congestion. Also includes trains that need to make additional stops or if there's a delayed connection. |
| NJT maintenance |  All tweets that blame delay on any programmed maintenance and track maintenance work done by NJ Transit. |
| NJT mechanical problem |  All tweets that blame delay on mechanical problems or mechanical issues in a NJ Transit train. |
| NJT operational issues |  All tweets that blame delay on "operational issues", including manpower shortage and delays because of bridge openings. |
| NJT signal problem |  All tweets that blame delay on signal problems in a NJ Transit train. |
| NJT switch problem |  All tweets that blame delay on switch problems in a NJ Transit train. |
| Police/Fire activity |  All tweets that blame delay on police or firefighter presence and includes tresspasser strikes and motor vehicle accidents. |
| Weather-related |  All tweets that blame delay on the weather, including downed trees or debris caught on wires. |

Sometimes, the tweets were very explicit in what caused the delay. However, there were a few times when the tweet was vague or incomplete or gave no explicit reason for the delay.

In those instances, we compared tweets that were sent during similar times from other connecting rail lines to try to figure out what was at fault. If we couldn’t figure out the reason, we labeled it as “no reason given." We are making the spreadsheet file of each scraped, filtered and categorized tweet available [here](https://github.com/CarlaAstudillo/NJ_Transit_Twitter_Analysis/blob/master/all_NJT_delay_march_april_may.csv). Let us know if you see any errors in how we categorized a tweet through [email](castudillo@njadvancemedia.com).
