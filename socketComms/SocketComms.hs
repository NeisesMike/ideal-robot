-- Echo server program
module SocketComms where

import Control.Concurrent (forkFinally)
import qualified Control.Exception as E
import Control.Monad (unless, forever, void)
import qualified Data.ByteString as S
import qualified Data.ByteString.Char8 as C
import Network.Socket hiding (recv)
import Network.Socket.ByteString (recv, sendAll)

portListen :: IO ()
portListen = withSocketsDo $ do
    addr <- resolve "3000"
    E.bracket (open addr) close loop
  where
    resolve port = do
        let hints = defaultHints {
                addrFlags = [AI_PASSIVE]
              , addrSocketType = Stream
              }
        addr:_ <- getAddrInfo (Just hints) Nothing (Just port)
        return addr
    open addr = do
        sock <- socket (addrFamily addr) (addrSocketType addr) (addrProtocol addr)
        setSocketOption sock ReuseAddr 1
        bind sock (addrAddress addr)
        listen sock 10
        return sock
    loop sock = do
        (conn, peer) <- accept sock
        putStrLn $ "Connection from " ++ show peer
        void $ forkFinally (talk conn) (\_ -> do close conn)
    talk conn = do
        msg <- recv conn 1024
        S.writeFile "/home/odroid/Documents/netcom/networksocket/socketComms/temp" msg
        unless (S.null msg) $ do
          sendAll conn msg
          talk conn

portSend :: String -> String -> IO ()
portSend myIP myMsg = withSocketsDo $ do
    addr <- resolve myIP "3000"
    E.bracket (open addr) close talk
  where
    resolve host port = do
        let hints = defaultHints { addrSocketType = Stream }
        addr:_ <- getAddrInfo (Just hints) (Just host) (Just port)
        return addr
    open addr = do
        sock <- socket (addrFamily addr) (addrSocketType addr) (addrProtocol addr)
        connect sock $ addrAddress addr
        return sock
    talk sock = do
        myInt <- send sock myMsg
        putStrLn $ show myInt
        msg <- recv sock 1024
        putStr "Received: "
        C.putStrLn msg
