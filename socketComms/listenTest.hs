import SocketComms
import Control.Concurrent
import qualified Data.ByteString as S
import qualified Data.ByteString.Char8 as C

main :: IO ()
main = do
        portListen
        threadDelay 1
        bString <- S.readFile "/home/odroid/Documents/netcom/networksocket/socketComms/temp"
        putStr "from client: "
        C.putStrLn bString
        putStrLn "end"
