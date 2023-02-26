<h1>QBot</h1>
<h4>A simple data collector for amusement park wait times</h4>

<p>Last summer, I visited Cedar Point hell bent on riding Millennium Force, consistently voted one of the best roller coasters in the nation. It was pretty much the only thing I rode all day. And maybe if I'd known that, I would have chosen to ride more of the world's slightly-less-than-best roller coasters that day. But Cedar Point's app said the wait was going to be 120 minutes, so I thought it was worth it. (It ended up being a little over 3 hours.)</p>

<p>I went into this project hoping to make an application that more accurately predicts wait times at amusement parks. I hoped to use a combination of official posted wait times, data from sites like <a href = http://www.queue-times.com>queue-times.com</a> or <a href="http://www.thrill-data.com">thrill-data.com</a>, and other available datasets to estimate this. However, I discovered that the existing data is pathetic. One website, for example, reported five minute waits all day on a Saturday in July.</p>

<p>There's a lot I'd love to do with a large amount of wait time data, so I decided to create an app that easily records wait time data for my later nefarious uses.</p>

<p>The app needed to be simple, easy to use in a busy park, and accurate to the second. It's much more simple than I originally wanted it to be, due to time constraints, getting distracted on a username/password system that wasn't necessary, and getting a crash-course in object-oriented programming.</p>

<p>The basics of the app are coded in Python, with a GUI created in Kivy. Ideally, this GUI could be packaged for Android and iOS. As of today, it writes the data it collects to a local .csv, but work is underway to connect it to a MySQL server for better security and reach.</p>

<p>Planned improvements include personal stats (number of credits, most rides on a single ride), auto-populated ride stats, and (obviously) the most accurate predicted ride times available to the public. This software will be kept free, ad-free, and open-source. I'm probably the only person who cares this much about this, but I can't be sure of that. Once I have a sizable dataset of queue times, it will be made available here.</p>

<p>Special thanks to Tech With Tim's <a href = "https://www.youtube.com/playlist?list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn">Kivy videos</a>, several key Stack Exchange questions, Garrett for the OOP crash course, and Sam for the moral support.</p>
