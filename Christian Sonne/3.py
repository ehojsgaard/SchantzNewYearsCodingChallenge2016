for x in range(1,13):print("On the %d%s day of Christmas\nmy true love sent to me:"%(x," snrttddh"[min(4,x)::4]),*("12 Drummers Drumming,Eleven Pipers Piping,Ten Lords a Leaping,Nine Ladies Dancing,Eight Maids a Milking,Seven Swans a Swimming,Six Geese a Laying,Five Golden Rings,Four Calling Birds,Three French Hens,Two Turtle Doves,"+["and a","A"][x<2]+" Partridge in a Pear Tree\n").split(",")[-x:],sep="\n")