import SocketComms
import Control.Concurrent

main :: IO ()
main = do
        portListen
        threadDelay 1
        bString <- readFile "/home/odroid/Documents/netcom/networksocket/socketComms/temp"
        putStr "from client: "
        putStrLn bString
        putStrLn "end"
