# Anim3u
Projeto para criar uma lista de reprodução diretamente no m3u

    usage: anim3u.py [-h] --link LINK [--start START] [--end END]

    optional arguments:
      -h, --help     Mostre esta mensagem de ajuda
      --link LINK    Link de um anime do site goyabu.com
      --start START  Episódio inicial
      --end END      Episódio final
      
### Exemplo:
    python3 anim3u.py --link https://goyabu.com/assistir/assistir-one-piece-online/ --start 10 --end 15

### Players que podem ser usados:
- [x] VLC Player
