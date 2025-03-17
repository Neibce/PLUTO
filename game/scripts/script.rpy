# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image 교실 = "bg_cs.png"
image 횡단보도 = "bg_cw.png"
image 옥상 = "bg_rt.png"
image 골목길 = "bg_aw.png"
image 공원 = "bg_pk.png"
image 눈 = "bg_sn.png"
image 배드엔딩 = "bg_be.jpg"
image 키스신 = "bg_ks.jpg"

image 샘 = "ch_tc_0.png"

image 여주 무표 = "ch_fp_0.png"
image 여주 웃음 = "ch_fp_1.png"
image 여주 슬픔 = "ch_fp_2.png"
image 여주 난처 = "ch_fp_3.png"
image 여주 화남 = "ch_fp_4.png"
image 여주 발그레 화남 = "ch_fp_4.png"
image 여주 이제안슬픔 = "ch_fp_0.png"

image 일진 일반 = "ch_ee_0.png"
image 일진 웃음 = "ch_ee_1.png"
image 일진 화남 = "ch_ee_2.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define mp = Character(_('박이안'), color="#FFF", namebox_background = Frame("gui/namebox_lblue.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define fp = Character(_('이아린'), color="#FFF", namebox_background = Frame("gui/namebox_purple.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define tc = Character(_('선생님'), color="#FFF", namebox_background = Frame("gui/namebox_lgreen.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define s1 = Character(_('지나가던 학생'), color="#FFF", namebox_background = Frame("gui/namebox_magenta.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define s2 = Character(_('지나가던 학생'), color="#FFF", namebox_background = Frame("gui/namebox_mint.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define ee = Character(_('일진'), color="#FFF")

init python:
    import urllib2
    from socket import timeout

    mpn=_("박이안")
    fpn=_("이아린")
    
    def requestAddNum(num):
        try:
            urllib2.urlopen('https://tcd-2018-pluto.azurewebsites.net/upload.php?slt='+num, None, timeout=2)
        except Exception:
            pass
    requestAddNum('')

#######################################################################
# Google Play Game Service 업적 관리를 위해 { renpy.vibrate(1.0) }
# 함수를 활용하여 파라미터 값이 1000.0 이상일때
# Vibrate 기능을 Google Play Game Service로 대체합니다.
#
# ex) renpy.vibrate(1001.0) -> '플레이 버튼을 찾았습니다!' 업적 달성.
#
#######################################################################

# 여기에서부터 게임이 시작합니다.
label start:
    play music "musics/flow.tcd" fadeout 2.0 fadein 5.0
    $quick_menu = False
    jump c0

label c0:
    scene black
    $ requestAddNum('0')
    $ renpy.vibrate(1001.0)
    if (persistent.ending1 and persistent.ending2 and persistent.ending3):
            $ renpy.vibrate(1008.0)
    window show
    "툭 투둑.."
    "쏴아아아아아아..........."
    "일기예보에도 없던 소나기가 갑자기 내리기 시작한다."
    "굵은 빗줄기들이 땅 위의 많은 것들을 씻어낸다."
    "비가 그치고 난 뒤에 땅위엔 다시 많은 것들이 쌓여간다. 선이든 악이든..."
    "우리는 비가 쓸고 간 자리에 무엇이 있었는지 알 수 없다."
    "설령,"
    "그것이 '희망'이라 할지라도 말이다..."
    "우리는 희망만 바라보며 살고 있다."
    "또한 그로 인해 가지지 못하는 많은 것들을 보며 절망한다..."
    "우리가 절망하는 건, 어쩌면 가지고 있는 것은 보지 못한 채, 가지지 못한 것만 바라보며 원하는 욕망의 산출물이 아닐까...."
    "그리고 이 사실을 깨달은 인간은 어떠한 태도를 가진 채 살아가야 할까.."
    "난 어떻게 살아가야 할까.."
    "난 어떻게 살아가야....."
    "난... 살아가야......"
    scene 교실
    with fade
    show 샘 at center:
        xalign 1.2
        yalign -0.3
        zoom 0.58
    with Dissolve(0.5)
    tc "[mpn], 잠 깨라."
    "난..................."
    tc "[mpn]! [mpn]! [mpn]!"
    mp "!!!! 네!!"
    tc "책상 앞에서 기도하지 말고! 69쪽 7번재 줄부터!"
    "(키득키득) "
    mp "아.. 안들리게 웃어주면 안되겠니 얘들아... 내가 지금 매우 쪽팔리니 말이야.."
    hide 샘
    with fade
    mp "... 네 ... 루소는..."
    "인간은 적응의 동물이다. 나 역시 '학급' 이라는 환경 안에서 '혼자' 라는 상황에 적응하였다.."
    "구차한 변명같아 보이지만, 나는 이 환경에 적절한 인간의 모습을 한 것이라고 생각한다..."
    mp "-- 싶은 것이다...."
    "아무도 듣지 않는 교과서 낭독을 마친 후 나는 내 자리에 앉았다.."
    "이제 다시 혼자만의 시간을 즐길 수 있겠군...."
    "............"
    ".........."
    "졸린다..."
    "............"
    "............ 일단 자야겠다......"
    
    scene black
    with fade
    "............"
    window hide
    jump c1

label c1:
    $ renpy.pause(1.0, hard=True)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 1. 빛과 그림자.{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    window show
    "평소에 하지 않는 일, 즉 비일상은 삶의 균형을 깨트린다."
    "비일상 때문에 내일의 일상, 혹은 더 먼 미래의 일상이 깨질 수 있다."
    "그런 의미에서는 재미없이 반복되는 일상.. 꽤 좋은 생각이지 않을까....."
    "이런 나의 신념을 실천하기 위하여 나는 오늘도 이어폰으로 두 귀를 틀어막고 내가 갈 길만을 본다."
    "누구도 나에게 관심을 주지 않고, 나도 아무에게도 관심을 주지 않는다."
    "이것이 나의 일상이다..."
    window hide
    scene 횡단보도
    with fade
    $ renpy.pause(1.0, hard=True)
    window show
    "비가 오는 하굣길.."
    "횡단보도 앞..."
    "자동차가 달리는 소리와 가끔씩 들려오는 경적소리..."
    "희미하게 들리는 그런 소리들을 음악소리로 내쫓아 버린다."
    "시선을 앞으로 고정한 채로 초록불이 켜지기 만을 기다리고 있는 때."
    "나와 같은 '그림자'를 보았다..."
    window hide
    with fade
    $ renpy.pause(2.0, hard=True)
    window show
    "검은 머리카락, 단아하지만 어두운 분위기, 주위에 퍼지는 깊고 진한 아픔..."
    "그림자다. 같은 교복이지만 주위의 웃고 떠들며 얘기하는 밝은 빛들의 검은 뒷면을 흡수한다."
    mp "뭐야..."
    "직감이다. 직감이 말해주고 있다. 뭔가 이상하다...."
    "안좋은 일이 일어날 것만 같다.... 따라가야 하나..."
    "..."
    window hide
    $ renpy.pause(1.5, hard=True)
    window show
    "초록불이 어느새 깜빡이고 있다."
    "6...5...4...3.....2.....1....."
    "젠장, 나의 일상이..."
    "횡단보도를 건너 그 여자아이를 찾기 시작했다..."
    "..."
    "..."
    "..."
    window hide
    scene 골목길
    with fade
    $ renpy.pause(1.5, hard=True)
    window show
    "골목길 안쪽에서 그녀를 찾았다."
    "다시 찾기 힘들지도 모른다.. 어떡하지"
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "빨리 달려가 팔을 붙잡는다..":
            if not persistent.menu1:
                $ persistent.menu1 = True
                $ requestAddNum('1_1')
            jump c1_1
        "따라가는 것을 포기한다..":
            if not persistent.menu1:
                $ persistent.menu1 = True
                $ requestAddNum('1_2')
            jump c1_2    

label c1_1:
    window show
    mp "저기..."
    $ renpy.vibrate(1.0)
    hide 여주 뒷모습
    with vpunch
    "꺄아아아아악!!!!!"
    "비명을 지르며 도망간다... 이게 아닌데..."
    window hide
    $ renpy.pause(1.0, hard=True)
    window show
    s1 "방금 무슨 상황이었냐?"
    s2 "몰라. 근데 쟤 7반 찐따 아니냐?"
    s1 "어 진짜네? 설마 지금 작업 건거냐? 역시 끼리끼리 논다더니.."
    s2 "여자애는 왜?"
    s1 "아, 걔는 학기 초에 일진한테 찍혔나봐. 먼저 싸가지 없게 대꾸했다던데..."
    s2 "재수도 없다. 쯧"
    s1 "한명은 싸가지, 한명은 찐따... 잘 어울리네.. 풋"
    "하아... 이게 아니었는데... 사과라도 해야 하려나...."
    window hide
    stop music fadeout 1.0
    scene black
    with dissolve
    play music "musics/bad.tcd"
    $ renpy.pause(2.0, hard=True)
    window show
    "위험을 무릅쓴 충동의 대가는 참혹하다...."
    "그 날 이후로 그녀를 계속 학교에서 찾아보았지만.. 끝내 찾을 수 없었다."
    "날 피해다닌 것일까...."
    "..."
    window hide
    $ renpy.pause(1.2, hard=True)
    window show
    "그리고 2달 뒤..."
    "학교의 여학생 한 명이 자살했다. 사인은 추락사..."
    "그 이후로 나는 졸업할 때까지 누구와도 말을 하지 않았다........"
    window hide
    scene black
    with fade
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    $ renpy.vibrate(1005.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Bad End 1.{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    if not persistent.ending1:
        $ persistent.ending1 = True
        if (persistent.ending1 and persistent.ending2 and persistent.ending3):
            $ renpy.vibrate(1008.0)
            "Chapter 3의 잠금이 해제되었습니다."
            $ renpy.pause(1.0, hard=True)
    return

label c1_2:
    window show
    "일단 나는 달리기를 멈췄다."
    "지금 당장 쫓아갈 필요는 없겠지.. 어차피 같은 학교니까 언젠가 돌아다니다 보면 마주칠테니까..."
    "나의 일상이 깨져버렸다. 아직 충분히 복구가 가능해 보인다......"
    "하지만 나의 신경은 모두 그 여자아이에게로 쏠려 있었다..."
    "...."
    "너무 많이 뛴 것 같다..."
    "..."
    "더 이상의 에너지 소모는 낭비다. 돌아가자..."
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    window show
    "나는 집으로 돌아갔다..."
    window hide
    $ renpy.pause(1.5, hard=True)
    window show
    "(다음 날)"
    scene 옥상
    with fade
    "학교 옥상..."
    "오늘은 바람이 상쾌하다. 소나기가 지나가서인가... 덕분에 옥상에서 느끼는 바람은 기분이 좋다."
    "옥상 오랜만이네..."
    "아직 적응하지 못했었을 때. 여기에 자주 오곤 했었다..."
    "..."
    "아무 생각없이 여기에 있다보면 마음이 안정되고는 했는데...."
    "..."
    "이상하게 오늘따라 쓸데없는 생각이 자꾸 머릿속에 떠오른다...."
    "검은 머리카락."
    "그림자..."
    "하아..........."
    "왜 지금 생각이 나는걸까. 갑자기 신경이 쓰인다.."
    "뭐. 괜찮게 생기기도 했지만 말이지..."
    window hide
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    window show
    "덜컥..."
    "갑자기 옥상 문이 열렸다..."
    "누구지?"
    play music "musics/ghost.tcd"
    "어?"
    "그 여자아이다..."
    "어제처럼 어두운 분위기를 풍기고 있다..."
    "..."
    "옥상에 올라와서 뭘 하려는 거지?"
    "이런 생각을 하고 있는 동안 그녀는 한치의 망설임도 없이 옥상의 끝을 향해 걸어가고 있었다."
    "... 설마?...."
    "위험하다... 저번보다 더 깊고 어두운 뭔가가 그녀를 덮고 있다..."
    "불안한 기운이 엄습해온다..."
    "어쩔 줄 몰라 망설이던 사이.."
    window hide
    with fade
    $ renpy.pause(1.0, hard=True)
    show 여주 난처:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    window show
    fp "아....."
    "이제야 내가 옥상에 있다는 사실을 알아챈 것 같다..."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "\"너... 뭘 하려는 거야?\"":
            if not persistent.menu2:
                $ persistent.menu2 = True
                $ requestAddNum('1_2_1')
            jump c1_2_1
        "\"저기... 안녕?\"":
            if not persistent.menu2:
                $ persistent.menu2 = True
                $ requestAddNum('1_2_2')
            jump c1_2_2

label c1_2_1:
    window show
    mp "너... 뭘 하려는 거야?" 
    show 여주 화남:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "짜증나게....(혼잣말)" 
    mp "뭐?" 
    fp "뭔데??" 
    mp "그.. 그게..."
    fp "니가 뭔데 갑자기 아는 척이야?" 
    mp "아니.. 난 그저..." 
    fp "신경 꺼..." 
    "..."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "옥상 밖으로 나간다.":
            if not persistent.menu3:
                $ persistent.menu3 = True
                $ requestAddNum('1_2_1_1')
            jump c1_2_1_1
        "사과한다...":
            if not persistent.menu3:
                $ persistent.menu3 = True
                $ requestAddNum('1_2_1_2')
            jump c1_2_1_2
    with Dissolve(.3)
                
label c1_2_1_1:
    scene black
    with fade
    window show
    "더 이상 아무 말도 하지 못하고 옥상 밖으로 나와 버렸다..." 
    mp "별...일 없겠지?......" 
    "나는 불안한 마음을 애써 무시하고 반쪽으로 발걸음을 옮겼다..." 
    scene 교실
    with fade
    "..." 
    "반에 도착했을 때... " 
    mp "아 맞다 엠피쓰리를 놔두고 왔네..." 
    "아직 시간은 충분하다. 빨리 다녀오면 될 것 같다...." 
    "..."
    window hide
    $ renpy.pause(1.0, hard=True)
    scene 옥상
    with fade
    window show
    "옥상에 다시 도착했을 때 문 사이로 그녀가 보였다..." 
    mp "어?"  
    "옥상 난간에 올라서려고 있는 모습을 보고 나서 아까 내가 그녀를 말렸어야 했다는 걸 깨달았다." 
    "곧바로 뛰어내리지 않는 걸 보니 망설이는 것 같다... 내가 말려야 하나?..."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "그녀에게 달려가 끌어당긴다...":
            if not persistent.menu4:
                $ persistent.menu4 = True
                $ requestAddNum('1_2_1_1_1')
            jump c1_2_1_1_1
        "가까운 선생님에게 알리러 간다...":
            if not persistent.menu4:
                $ persistent.menu4 = True
                $ requestAddNum('1_2_1_1_2')
            jump c1_2_1_1_2

label c1_2_1_1_1:
    "생각하기도 전에 몸이 먼저 반응했다..." 
    "탁탁탁!!!" 
    mp "안돼!!!!!!!"
    $ renpy.vibrate(1.0)
    scene 옥상
    with vpunch
    "쿠당탕......."
    window hide
    $ renpy.pause(1.0, hard=True)
    show 여주 난처:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with dissolve
    window show
    "!!!!" 
    stop music fadeout 2.0
    mp "너 미쳤어??" 
    fp "뭐..뭐야 너 어떻게 알고??"
    mp "어떻게 알았냐고? 옥상 난간에서 그렇게 이상한 기운을 풍기면서 서 있는데 모르겠냐?! 나랑 같으니까!!" 
    mp "그리고.. 그 전부터 보였다고... 너한테 깔린 '그림자' 말이야..."
    
    "하아..................." 
    "........" 
    mp "다른 사람들한테는 비밀로 할 테니까.. 다시는 이런 짓 하지마, 알았어?" 
    show 여주 무표:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    "..." 
    "대답 없이 끄덕이는 그녀..." 
    "..." 
    "..." 
    "어색한 침묵이 두 사람 사이에 흐른다." 
    "..." 
    "..." 
    "이런 어색함을 이기지 못하고 먼저 입을 열었다..." 
    play music "musics/flow.tcd" fadein 3.0
    mp "그래서.. 저기... 이름이 뭐야? 아직까지 이름도 몰랐네........" 
    fp "...........[fpn].... 8반..." 
    mp "난 [mpn]. 7반이야..잘 부탁해.." 
    show 여주 웃음:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "…잘 부탁해? 풋..." 
    mp "에?" 
    fp "부탁하긴 뭘 부탁해." 
    mp "아.. 그런가?.." 
    "...." 
    "...." 
    "다시 둘 사이에 침묵이 흐른다..." 
    "하지만 아까보다는 분위기가 괜찮아진 것 같다." 
    window hide
    $ renpy.pause(1.0, hard=True)
    window show
    "...조심스레 다시 그녀에게 묻는다." 
    mp "다시는 그러지 않을 거지?" 
    fp "...응" 
    mp "다행이네, 다시 살아갈 마음이 생긴 거 같으니까." 
    fp "고...마워." 
    "그녀가 웃고 있다... 아직 슬픔과 절망이 가득하지만, 한줄기 빛을 발견한 듯이, 은은하게 " 
    "빛나는, 고요 속의 물방울 하나와 같이 아름답다. 정말 아름답다...." 
    "쓸데없는 감정낭비는 피곤해지기만 한다." 
    "..." 
    "이렇게 나의 일상은 완전히 깨지고 말았다." 
    "깨져버린 나의 일상은 더 이상 돌아오지 않을 것 같다..."
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 1. 빛과 그림자.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    with fade
    $ renpy.pause(2.0, hard=True)
    jump c2

label c1_2_1_1_2:
    scene black
    with fade
    window show
    "...빨리 ...빨리 아무 선생님이나....."
    "옥상 난간 위에 서 있는 그녀를 두고 아래층으로 달려갔다."
    scene 교실
    show 샘 at center:
        xalign 1.2
        yalign -0.3
        zoom 0.58
    with fade
    mp "헉..헉.... 선생님..!"
    tc "왜? 뭐 때문에 그리 급하게 뛰어왔냐?" 
    "최대한 빨리 상황을 설명하고 선생님과 함께 옥상으로 올라갔다....."
    window hide
    hide 샘
    with Dissolve(0.5)

    $ renpy.pause(1.0, hard=True)
    scene 옥상
    with fade
    window show
    tc "!! [fpn]! 너 지금 뭐하는ㄱ........."
    stop music fadeout 1.0
    "...!!"
    play music "musics/bad.tcd"
    "선생님이 그녀에게 소리치는 순간 그녀의 몸이 사라졌다.... " 
    "...쿵...."
    "무거운 물체가 바닥에 부딪히는 소리가 난다..."
    window hide
    scene black
    with fade
    $ renpy.pause(2.0, hard=True)
    scene 배드엔딩
    with fade
    window show
    "..."
    "막지.. 못했다... " 
    "막을 수... 있었는데..." 
    "나.. 나 때문에...."
    "..."
    "내가 아까 곧바로 붙잡았더라면........." 
    "..."
    window hide
    scene black
    with fade
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    $ renpy.vibrate(1006.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Bad End 2.{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    if not persistent.ending2:
        $ persistent.ending2 = True
        if (persistent.ending1 and persistent.ending2 and persistent.ending3):
            $ renpy.vibrate(1008.0)
            "Chapter 3의 잠금이 해제되었습니다."
            $ renpy.pause(1.0, hard=True)
    return


label c1_2_1_2:
    window show
    mp "미안해. 기분 상하게 할 생각은 없었어." 
    "나는 고개 숙여 사과했다.." 
    show 여주 난처:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "어? 그렇게 사과할 것까지는...." 
    stop music fadeout 3.0
    "..........." 
    "..............." 
    "어색한 침묵만이 나와 그녀, 둘 사이에 흐른다."
    window hide
    $ renpy.pause(2.0, hard=True)
    window show
    ".. 언제까지 이러고 있어야 하지?" 
    "내가 먼저 말을 꺼내야 하나...." 
    "...그래.. 먼저 말을 하자." 
    "..." 
    play music "musics/flow.tcd"
    mp "저기..." 
    "...왜?"
    mp "아까... 왜 그런 말을 했냐면..... 네 얼굴에 그림자가 드리워져 있었어... 아주 어두운 그림자.." 
    fp ".....!!" 
    "내가 무슨 말을 했는지 이해한 것 같다." 
    fp "그럼.... 알고 있는 거야? 내가 뭘 하려 했는지?" 
    mp ".... 느낌일 뿐이지만...." 
    "(잠깐의 적막..)" 
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "재밌네..." 
    mp "어?"
    fp "너 말이야. 진짜 재밌는 애구나?.. 근데... 그거 알아? 너도 얼굴에 그림자가 가득해." 
    mp "아마도.. 그렇겠지..." 
    "..." 
    fp "난 [fpn] 8반이야. 너는?" 
    mp "[mpn]... 7반" 
    fp "바로 옆반이었네? 앞으로 친하게 지내자." 
    mp "응..." 
    "...잘 지내자고 해봤자... 말뿐이겠지..." 
    "얘기가 끝났다고 생각한 나는 고개를 들었다." 
    "아까처럼 무표정일 것이라고 생각했지만, 그녀는 웃고 있었다." 
    "어두운 세상 안에서 한줄기 빛을 찾은 것처럼 해맑게 웃고 있는 그녀의 미소가 " 
    "아름답다. 정말로...." 
    "..." 
    "쓸데없는 감정 낭비는 피곤해지기만 한다." 
    "..." 
    "이렇게 나의 일상은 완전히 깨지고 말았다." 
    "깨져버린 나의 일상은 더 이상 돌아오지 않을 것 같다..."
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 1. 빛과 그림자.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    with fade
    $ renpy.pause(2.0, hard=True)
    jump c2

label c1_2_2:
    show 여주 난처 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    mp "저기... 안녕?" 
    "......" 
    mp "......하하..." 
    fp "......그래, 안녕." 
    mp "…음...이름이 뭐야?" 
    fp "...[fpn]" 
    mp "오, 그렇구나. 난 [mpn]이야. 잘 부탁해."
    stop music fadeout 3.0
    hide 여주 난처
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "풉, 잘...부탁해?" 
    mp "에?" 
    fp "부탁하긴 뭘 부탁해." 
    mp "아...아, 하하하..." 
    "......" 
    "......" 
    "... 어색하다.." 

    "굉장히 어색하다. 하지만 경멸의 느낌은 아니다." 
    "적어도 하나의 인간으로 봐주고 있는 것 같다." 
    "지금 이때라면 말할 수 있지 않을까."
    play music "musics/flow.tcd" fadein 3.0
    mp "저기..." 
    fp "...왜?" 
    mp "얼굴에, 그림자가 드리워져 있었어... 굉장히 어두운 그림자."
    show 여주 난처 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "......알고 있는 거야? 내가 뭘 하려고 했는지?" 
    mp "...느낌일 뿐이지만." 
    "(잠깐의 적막..)" 
    hide 여주 난처
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    
    fp "재밌네...(혼잣말)" 
    mp "어?"
    fp "너 말이야. 진짜 재밌는 애구나?.. 근데...그거 알아? 너도 얼굴에 그림자가 가득해."

    mp "아마도.. 그렇겠지..." 
    "..." 
    fp "난 [fpn] 8반이야. 너는?" 
    mp "[mpn]... 7반" 
    fp "바로 옆반이었네? 앞으로 친하게 지내자." 
    mp "응..." 

    "...잘 지내자고 해봤자... 말 뿐이겠지..." 
    "얘기가 끝났다고 생각한 나는 고개를 들었다."
    "아까처럼 무표정일 것이라고 생각했지만, 그녀는 웃고 있었다." 
    "어두운 세상 안에서 한 줄기 빛을 찾은 것처럼 해맑게 웃고 있는" 
    "그녀의 미소가 아름답다. 정말로...." 
    "..." 
    "쓸데없는 감정낭비는 피곤해지기만 한다." 
    "..." 
    "이렇게 나의 일상은 완전히 깨지고 말았다." 
    "깨져버린 나의 일상은 더 이상 돌아오지 않을 것 같다... "
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    $ renpy.vibrate(1002.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 1. 빛과 그림자.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    with fade
    $ renpy.pause(2.0, hard=True)
    jump c2

label c2:
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 2. 레지스탕스.{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    window show
    "옥상은 언제나 나에게 고독의 장소로만 쓰여져 왔다."
    "하지만 요즘 그 고독만이 있던 장소에 따뜻한 무언가가 느껴진다.." 
    scene 옥상
    with fade
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    fp "그래서, 내가 말이야..."
    "2달이 지난 뒤, 그녀는 눈에 띄게 밝아졌다."
    "예전에는 말조차 하기 싫어했지만, 이제는 자기 얘기도 서슴없이 하게 되었다."
    window hide
    $ renpy.pause(0.5, hard=True)
    hide 여주 웃음
    with Dissolve(0.5)
    $ renpy.pause(1.0, hard=True)
    window show
    "그녀가 옆에 있었던 게 부담스러웠지만,"
    "어느새 그녀와 함께 이야기하고 함께 웃는 게 일상이 되어버렸다...."
    ".." 
    "깨져버린 일상, 그리고 그게 나의 '일상'이 되어간다." 
    "... 혹시 나는 그녀를 '좋아하고' 있는 것일까?" 
    "그저 그녀와 같은 아픔을 가진 '그림자'이기 때문일까..." 
    "만약, 만약에 말이다. 진짜 '좋아하는'거라면 난 어떻게 해야 하지?..."
    window hide
    $ renpy.pause(0.7, hard=True)
    show 여주 무표 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    window show
    fp "맞다. 있잖아."
    "바보같은 생각을 하던 중 갑자기 질문이 날아왔다." 
    fp "나무젓가락 하나는 잘 부러지잖아.." 
    mp "응." 
    fp "그리고 나무젓가락이 많으면 잘 안 부러지잖아.." 
    mp "응." 
    fp "그럼 나무젓가락 두 개는 잘 부러질까?" 
    mp "... 잘 모르겠는데.." 
    fp "그냥 대답해봐. 빨리.." 
    mp "나는..."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "\"두 개라도 잘 부러지지 않을까?\"":
            if not persistent.menu5:
                $ persistent.menu5 = True
                $ requestAddNum('2_1')   
            jump c2_1
        "\"두 개 정도면 안 부러질 거 같은데?\"":
            if not persistent.menu5:
                $ persistent.menu5 = True
                $ requestAddNum('2_2') 
            jump c2_2

label c2_1:
    window show
    mp "두 개라도 잘 부러지지 않을까?" 
    fp ".... 그래?.."
    mp "응.." 
    fp ".. 알겠어.." 
    "순간 어두워진 얼굴. 무엇을 의미한 걸까..."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "아무 말도 하지 않는다.":
            if not persistent.menu6:
                $ persistent.menu6 = True
                $ requestAddNum('2_1_1')
            jump c2_1_1
        "\"그래도 하나보단 둘이 낫지 않을까?\"":
            if not persistent.menu6:
                $ persistent.menu6 = True
                $ requestAddNum('2_1_2')
            jump c2_1_2


label c2_1_1:
    window show
    fp "... 괜히 이상한 질문 해서 미안해." 
    mp "딱히? 이상하진 않았는데??" 
    fp "....... 가자. 종 쳤어.."
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    window show
    "어떤 의도로 나에게 그 질문을 던진 것일까.. 모르겠다.. 궁금하다... 답답하다.. " 
    "..." 
    "그 뒤로 2주간 [fpn]은 학교에 오지 않았다." 
    "어째서... 점점 밝아지고 있었잖아..." 
    "..."
    window hide
    $ renpy.pause(1.0, hard=True)
    scene 교실
    with fade
    show 여주 무표 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    window show
    "월요일 아침시간, 우연히 그녀와 만났다." 
    mp "어, [fpn]." 
    "반갑게 인사한다." 
    fp "안녕..." 
    fp "어디 가는 길이야..?" 
    mp "나 어디 가봐야 할 데가 있어서... 너는?" 
    fp "나? 전학 신청서...."
    hide 여주 무표
    with Dissolve(0.5)
    "전학 신청서. 전학 신청서. 전학 신청서. 전학 신청서.." 
    "그 단어가 내 머릿속을 맴돌기 시작했다." 
    window hide
    $ renpy.pause(1.5, hard=True)
    show 여주 무표 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    window show
    mp "어디로 가는 거야?" 
    fp "캐나다로 유학 가. 아마 아주 오랫동안 못 볼 거야." 
    mp "그렇구나..." 
    fp "이제 나도 나'답게' 살아야지. 그럼 나 먼저 가볼게." 
    mp "그래......" 
    hide 여주 무표
    with Dissolve(0.75)
    "그녀가 떠나간다. 붙잡고 싶다. 하지만, 나는 그럴 자격이 없다." 
    "나'답게'. 너'답게'. 사람'답게'." 
    "이것의 진정한 의미는 무엇인가. 우리는 이것들을 정의할 수 있을까..." 
    "우리는 찾을 수 없는 것을 찾고 있는 게 아닐까..." 
    mp "나'답게' 라니, 그건 아니야..."
    stop music fadeout 1.5
    "..."
    window hide
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    play music "musics/ghost.tcd"
    window show
    "잠깐만. 교무실은 2층인데?..!!" 
    "뒤돌아서 그녀를 향해 뛰어간다. 젠장.."
    mp "설마... 설마......" 
    "헉...헉...." 
    "옥상으로 가는 길이 오늘따라 이상하게 무섭다..." 
    "도착했다..."
    "쾅!" 
    "나는 옥상 문을 급하게 열었다..." 
    "..."
    window hide
    $ renpy.pause(0.7, hard=True)
    scene 옥상
    with fade
    window show
    "두 달 전과 똑같이 그녀는 옥상 난간에 서 있다.." 
    "그때와 하나 다른 점은..."
    "그녀는 그 전과는 달리 한치의 망설임도, 두려움도 보이지 않았다....."
    stop music fadeout 0.7
    mp "안돼...!!!"
    play music "musics/bad.tcd"
    "..쿵" 
    "..." 
    window hide
    scene black
    with fade
    $ renpy.pause(2.0, hard=True)
    scene 배드엔딩
    with fade
    window show
    "아스팔트 냄새. 피 냄새. 웅성거리는 소리." 
    "구급...차... 소리......" 
    "그리고.." 
    "적막...."
    window hide
    scene black
    hide 여주 뒷모습
    with Dissolve(1)
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    $ renpy.vibrate(1007.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Bad End 3.{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    if not persistent.ending3:
        $ persistent.ending3 = True
        if (persistent.ending1 and persistent.ending2 and persistent.ending3):
            $ renpy.vibrate(1008.0)
            "Chapter 3의 잠금이 해제되었습니다."
            $ renpy.pause(1.0, hard=True)
    return

label c2_1_2:
    mp "그래도 하나보단 둘이 낫지 않을까?"
    $ ans1 = _("그래도 하나보단 둘이 낫지 않을까?")
    $ ans2 = _("하나보단 둘이 나을거라고..")
    "어두워진 그녀의 얼굴을 보고 싶지 않았기에 나는 다시 말했다..."

    show 여주 난처 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92

    fp "어?"
    mp "분명히 나무젓가락 두 개라도 부서질거야..."
    mp "하지만 하나만 부서진다면 다시 쓸 수 없을 정도로 망가지겠지만, 두 개라면... 조금은 덜 부서지겠지..."
    fp "....."
    mp "그러니깐 어떻게든 다시 쓸 수 있지 않을까?"
    fp "흠...."
    mp "아닌가?"
    hide 여주 난처
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    fp ".. 넌 정말 그렇게 생각해?"
    mp "응."
    fp "좋아.. 알겠어."
    "... 오늘따라 그녀가 달라보인다. "
    "결의에 차 있는 눈동자... 이제까지 본 모습중에 가장 다른 모습이다..."
    mp "..."
    mp "질문의 진짜 의도가 뭐였을까..."
    fp "아 참, 그리고.."
    mp "뭔데?"
    fp "나'답게' 사는 것이 뭘까?"
    mp "또 어려운 질문이다. 나'답게'.... 몇 번이고 생각해본 질문이기도 하다. "
    "대답할 수가 없다... 난 그것을 알지 못한다. 하지만,"
    mp "자기가 정말 원하는 방향으로 삶을 만들어 나가는 게 나'답게'가 아닐까?"
    fp "멋있는 말이네."
    mp "아니, 뭐, 그럴 거까지는..."
    "윽... 부끄럽다. 괜히 이런 말을 한 것 같다."
    "그래도, 이게 그토록 바라던 정답 중 하나가 아닐까."
    "..."
    jump c2_3

label c2_2:
    show 여주 난처 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    mp "두 개 정도면 안 부러질 거 같은데?"
    $ ans1 = _("두 개 정도면 안 부러질 거 같은데?")
    $ ans2 = _("두 개라면 부러지지 않을거라고..")
    fp "흠...." 
    mp "아닌가?" 
    fp " .. 넌 정말 그렇게 생각해?" 
    mp "응." 
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "좋아.. 알겠어."
    window hide
    hide 여주 웃음
    with Dissolve(0.7)
    window hide
    $ renpy.pause(0.7, hard=True)
    window show
    "... 오늘따라 그녀가 달라 보인다." 
    "결의에 차 있는 눈동자... 이제까지 본 모습 중에 가장 다른 모습이다..." 
    "..." 
    "질문의 진짜 의도가 뭐였을까..." 
    show 여주 무표 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(.5)
    fp "아 참, 그리고.." 
    mp "뭔데?" 
    fp "나'답게' 사는 것이 뭘까?" 
    "또 어려운 질문이다. 나'답게'.... 몇 번이고 생각해본 질문이기도 하다." 
    "대답할 수가 없다... 난 그것을 알지 못한다. 하지만," 
    mp "자기가 정말 원하는 방향으로 삶을 만들어 나가는게 나'답게'가 아닐까?" 
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.35)
    fp "멋있는 말이네." 
    mp "아니, 뭐, 그럴 거까지는..." 
    hide 여주 웃음
    with Dissolve(0.35)
    "윽... 부끄럽다. 괜히 이런 말을 한 것 같다." 
    "그래도, 이게 그토록 바라던 정답 중 하나가 아닐까." 
    "..."
    jump c2_3    

label c2_3:
    "그리고 며칠 뒤, 나는 질문의 의도를 알아차리게 되었다."
    window hide
    scene 교실
    with fade
    window show
    s1 "야, 야, 8반에서 여자애들끼리 싸운다."
    "8반? 8반이면,"
    "설마...?"
    "급히 달려간다. 설마, 설마."
    s1 "쟤 뭔데 저래 달려가냐?"
    s2 "쌈 구경이 재밌나 보지. 냅둬. 우리도 보러 가자."
    "설마."
    window hide
    with fade
    $ renpy.pause(1.0, hard=True)
    show 일진 웃음 at center:
        xalign 0.15
        yalign 1.0
        zoom 0.92
    show 여주 화남 at center:
        xalign 0.82
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    $ renpy.pause(1.0, hard=True)
    window show
    fp "싫어!!!"
    ee "아주 지랄을 떤다. 그리고 고함이나 빽빽 지르지 말아줄래? 존나 시끄럽거든??"
    "[mpn]과 맞은편은 일진 패거리들이다. 남자 일진들은 재미난 구경이라도 난 듯 뒤로 빠져 있다."
    fp "그만 괴롭히라고!!!"
    ee "이 새끼 뭐냐?? 지가 맞을 짓을 해놓고 이제와서 개기시겠다?"
    "다리를 떨고 있다. 무서워하잖아. 어째서 갑자기 그러는 거......"
    "..."
    "아. 그때의 대화."
    window hide
    scene 옥상
    with Dissolve(0.7)
    $ renpy.pause(1.0, hard=True)
    window show
    show 여주 웃음 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.7)
    mp "[ans1]"
    fp "넌, 정말 그렇게 생각해?"
    mp "응."
    hide 여주 웃음
    with Dissolve(0.7)

    "이제야 의미를 알았다."
    window hide
    $ renpy.pause(1.5, hard=True)

    scene 교실
    show 여주 화남 at center:
        xalign 0.82
        yalign 1.0
        zoom 0.92
    show 일진 일반 at center:
        xalign 0.15
        yalign 1.0
        zoom 0.92
    with Dissolve(0.7)

    window show
    "저항의 암시. 소수의 단합력. 나무젓가락은 그녀와 나를 의미한 것이었다."
    "저항한다. 저항하고 있다. 나는 그 저항에 믿음을 실어주었다."
    "난 믿음을 실어준 만큼, 추진력을 제공해준 만큼, 아니 그 이상,"
    "보답을 보여주어야 한다고 생각한다."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "앞을 막아선다.":
            if not persistent.menu7:
                $ persistent.menu7 = True
                $ requestAddNum('2_3_1')
            jump c2_3_1
        "손을 잡고 교실 밖으로 나간다.":
            if not persistent.menu7:
                $ persistent.menu7 = True
                $ requestAddNum('2_3_2')
            jump c2_3_2

label c2_3_1:
    window show
    "지금까지의 나는 저항하지 않았다고 해도," 
    "미래에도 그렇게 되어 버릴지도 몰라도.." 
    "이 순간만큼은," 
    "그녀와 함께 저항하는 '레지스탕스' 다." 
    "나는 나의 모든 용기, 의지를 끌어모아 그녀 앞에 섰다." 
    mp "그만해."
    ee "넌 뭔데?"
    mp "친구다. 그만해. 싫다고 하잖아."
    $ renpy.vibrate(1.0)
    show 일진 화남 at left: 
        xalign 0.15
        yalign 1.0
        zoom 0.92
    show 여주 난처 at center:
        xalign 0.82
        yalign 1.0
        zoom 0.92
    with vpunch
    ee "니가 뭔데 끼어들고 지랄이야!!" 
    "......." 
    "대답 대신 그 녀석을 똑바로 바라봤다." 
    "... 수군수군" 
    s1 "조금 심한 거 같은데..." 
    s2 "그러니까.. 저렇게까지 하고싶나?" 
    s1 "적당히 좀 하지... 근데 쟤네들 진짜 사귀는거야?"
    window hide
    $ renpy.pause(1.5, hard=True)
    window show
    "수군대는 소리가 더 커지기 시작한다." 
    "처음의 불씨는 작고 약하다... 너무 약해서 시작하기도 전에 꺼져버리고 만다..." 
    "하지만 그 불씨들이 하나로 모이게 된다면. " 
    "불씨는 불꽃이 된다..." 
    "불꽃은 또 다른 불꽃을 만들어내고," 
    "불꽃들은 더 큰 불길을 만들어낸다..." 
    "..." 
    ee "씨X.... 너네 둘 두고보자..." 
    hide 일진 화남
    hide 여주 난처
    with fade
    "그렇게 말하고는 자기 패거리들이 있는 곳으로 가버린다." 
    "..." 
    "나, 방금 무슨 짓을 한 거지? 어디서 그런 용기가.." 
    "10분 전의 나로서는 상상도 못할 일이다..." 
    show 여주 이제안슬픔 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.3) 
    mp "[fpn], 괜찮아?" 
    fp "....고마워...." 
    mp "혼자가 아니니까... 함께 있다면 더 이상 상처받지 않아도 돼..." 
    fp "....응" 
    "..." 
    "신기하다.. 이런 느낌. 언제나 현실에 순응해버린 나에게 이런 변화는 낯설게만 느껴진다..."
    window hide
    scene black
    with fade
    hide 여주 안슬픔
    window hide
    stop music fadeout 3.0
    $ renpy.pause(1.0, hard=True)
    $ renpy.vibrate(1003.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 2. 레지스탕스.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    with fade
    jump c3
    
label c2_3_2:
    window show 
    "그녀의 곁에 다가가 손을 잡고 그대로 교실 밖으로 나간다."
    mp "가자."
    show 여주 난처 at center:
        xalign 0.82
        yalign 1.0
        zoom 0.92
    with Dissolve(0.2)
    fp "어?..."
    $ renpy.vibrate(1.0)
    show 일진 화남 at right:
        xalign 0.15
        yalign 1.0
        zoom 0.92
    with vpunch

    ee "넌 뭐야! 이 새끼가 돌았나! 사람이 말을 하는데!!..."
    ee "야 너.......가만......둬!.."
    window hide
    hide 일진 화남
    hide 여주 난처
    with fade
    $ renpy.pause(1.5, hard=True)
    window show
    "..."
    "..."
    "충분히 멀어진 것 같다...."
    show 여주 화남 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.5)
    fp "왜 도망친거야! 이제야 혼자서 이겨 낼 수 있게 됐는데.."
    mp "........꼭 그런 식으로 저항할 필요 없어."
    mp "왜 너만 상처받아야 하는건데?"
    show 여주 슬픔 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    with Dissolve(0.4)
    fp "......"
    mp "하아.. 내가 그랬잖아. [ans2]"
    mp "그러니까, 혼자 상처받을 필요없어."
    show 여주 이제안슬픔 at center:
        xalign 0.5
        yalign 1.0
        zoom 0.92
    fp "응....."
    fp "그리고...고마워..."
    hide 여주 이제안슬픔
    with Dissolve(0.8)
    window hide
    $ renpy.pause(1.0, hard=True)
    window show
    "..."
    "그녀가 믿고 의지할 수 있는 그런 사람이 되고싶다."
    "... 처음으로 현실에 저항했다..."
    "신기하다.. 이런 느낌.. 언제나 현실에 순응해버린 나에게 이런 변화는 낯설게만 느껴진다..."
    window hide
    scene black
    with fade
    stop music fadeout 3.0
    $ renpy.pause(1.0, hard=True)
    $ renpy.vibrate(1003.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 2. 레지스탕스.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    with fade
    jump c3

label c3:
    if not (persistent.ending1 and persistent.ending2 and persistent.ending3):
        call screen play_again

    play music "musics/ED.tcd" fadein 5.0
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 3. '답지 않게'.{/size}{/cps}{/color}{/b}"
    scene 눈
    with fade
    $ renpy.pause(1.0, hard=True)
    window show
    "..."
    "한 학기가 지나고 겨울이 왔다."
    "'그 사건' 이후로 나와 그녀에게는 친구들이 생기기 시작했다."
    "주로 일진들에게 불만이 많은 친구들이었다."
    window hide
    $ renpy.pause(1.0, hard=True)
    window show
    "그리고 그동안 그녀와 더 가까운 사이가 되었다."
    "그녀가 바라고, 내가 바랐던 대로."
    "우리는 '혼자'가 아닌 '함께'가 되었다..."
    window hide
    with fade
    window show
    "그리고.... "
    "겨울방학이 시작되면서 한동안 그녀와 만나지 못했다."
    "..."
    "개학이 하루 남은 일요일..."
    "친구 녀석들이랑 마지막으로 놀고 집으로 돌아오던 도중.."
    "우연히 그녀와 마주쳤다..."
    window hide
    scene 공원
    with fade
    $ renpy.pause(2.0, hard=True)
    show 여주 이제안슬픔 at center:
       yalign 1.0
       zoom 0.92
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    window show
    fp "... 안녕..."
    mp ".....응 오랜만이네."
    "벤치에 나란히 앉았다..."
    hide 여주 이제안슬픔
    with Dissolve(0.3)
    ".........."
    "........"
    window hide
    $ renpy.pause(2.0, hard=True)
    show 여주 이제안슬픔 at center:
       yalign 1.0
       zoom 0.92
    with Dissolve(0.5)
    $ renpy.pause(1.0, hard=True)
    window show
    fp ".........저기..."
    "오랜 정적 속에 먼저 ---[fpn]이 말을 꺼냈다."
    fp "나는, 무언가 '답지 않게' 살 거야."
    "'답지 않게'. 그렇다. 이것이 바로 정답이었을 것이다."
    "나는 나고, 남은 남이다. 하지만 나'답게' 라는 것은 없다.."
    mp "그래."
    fp "이젠 다른 사람 때문에 나'답게' 살려고 애쓰지 않을거야..."
    mp "'그때'의 넌 너'답지 않게' 행동했었으니까..."
    fp "맞아... 너 덕분에.. 지금까지 버텨낼 수 있었어… "
    mp "뭐..."
    "그녀의 눈가가 촉촉히 젖어간다..."
    fp "사실 너무 무서웠어." 
    fp "두렵고, 외롭고, 무서웠어. 혼자가 아니라는 게 그렇게 고마운 건지 그때 처음 알았어."
    fp "니가 앞에서, 날 위해서 같이 싸워주는 게...... 너무 고마웠어."
    fp "나...나... 무섭고,,,,,,힘들어서......(훌쩍)......"
    "나도 무서웠다고 말하고 싶다. 겁먹고, 사회에 순응하는 편이 나은 것이라 생각했다."
    "용기내서 말한다는 것은 너무나도 힘든 법이다."
    "그래도, 곁에 있어줘서, 고맙다고, 정말 고맙다고 말해주는 게 너무 아파서 차마 말을 못하겠다."
    mp "괜찮아. 다 지났잖아."
    fp "(훌쩍)............"
    window hide
    $ renpy.pause(1.0, hard=True)
    window show
    "비는 모든 것을 씻어낸다. 그것이 희망일지라도."
    "하지만 우리는 희망을 믿음으로써 절망 속에서도 희망을 바란다. 그것이 현실이 될 때 우리는 행복해 질 수 있다."
    "..."
    " 그림자가 있기에 빛이 있고, 절망이 있기에 희망이 있다."
    "'우리'는 그림자 속에서 빛을 찾아냈다. 절망 속에서 희망을 찾아냈다."
    "토닥토닥. 지금까지 수고했다고 위로해준다."
    "얼굴을 마주본다."
    "지금이라면,"
    "지금이라면.."
    "나의 모든 마음을 그녀에게 보여줄 수 있을 것 같다."
    "'좋아한다'는 내 마음을 그녀에게 보여주고 싶다."
    "나도, 나'답지 않게' 살 거야."
    window hide
    $ renpy.pause(0.5, hard=True)
    menu:
        "내가 먼저 키스한다.":
            if not persistent.menu8:
                $ persistent.menu8 = True
                $ requestAddNum('3_1')
            jump c3_1 
        "역시.. 키스는 무리일까...":
            if not persistent.menu8:
                $ persistent.menu8 = True
                $ requestAddNum('3_2')
            jump c3_2
            
label c3_1:
    window show
    "눈이 마주친다."
    "내가 먼저 그녀에게 다가가 키스한다."
    "..."
    window hide
    scene 키스신
    with fade
    $ renpy.pause(2.0, hard=True)
    window show
    "쓰고 비린 시절을 지나, 촉촉하고 달콤한, 정말 진한,"
    "주위의 눈을 녹게 할 듯한 입술과 입술의 만남."
    window hide
    stop music fadeout 3.0
    $ renpy.pause(1.0, hard=True)
    scene black
    with fade
    $ requestAddNum('3_C')
    $ renpy.pause(2.0, hard=True)
    $ renpy.vibrate(1004.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 3. '답지 않게'.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    play music "musics/aday.tcd" fadein 3.0
    call screen credits

label c3_2:
    window show
    "눈이 마주친다."
    "..."
    "역시 먼저 키스하는건... 무리일까.."
    "라고 생각하는 순간 그녀가 먼저 입을 맞춰온다.."
    "!!"
    "..."
    window hide
    scene 키스신
    with fade
    $ renpy.pause(2.0, hard=True)
    window show
    "쓰고 비린 시절을 지나, 촉촉하고 달콤한, 정말 진한,"
    "주위의 눈을 녹게 할 듯한 입술과 입술의 만남."
    window hide
    stop music fadeout 3.0
    $ renpy.pause(1.0, hard=True)
    scene black
    with fade
    $ requestAddNum('3_C')
    $ renpy.pause(2.0, hard=True)
    $ renpy.vibrate(1004.0)
    centered "{b}{color=#ccc}{cps=*0.4}{size=+7}Chapter 3. '답지 않게'.\n{w=0.7}- End -{/size}{/cps}{/color}{/b}"
    $ renpy.pause(1.0, hard=True)
    play music "musics/aday.tcd" fadein 3.0
    call screen credits

screen play_again():
    imagebutton:
        idle Color((0, 0, 0, 0))
        clicked Jump("end")
    vbox:
        xalign 0.5
        yalign 0.5
        text _("{color=#fff}엔딩을 모두 본 후에\nChapter 3을 플레이 할 수 있습니다.{/color}"):
            size 50
        null height 30
        $c = [persistent.ending1,persistent.ending2,persistent.ending3].count(True)
        text _("{color=#fff}지금까지 본 엔딩: [c]/3{/color}"):
            xalign 0.5
            size 30
        null height 36

transform credits_scroll(speed):
    ypos 720
    linear speed ypos -2200

screen credits():
    timer 38.0 action Jump("credits_end")
    style_prefix "credits"
    add "#000"

    frame at credits_scroll(38.0):
        
        background None
        xalign 0.5
        vbox:
            text "Pluto" style "title"

            text "Team Coding Dongcheon 2018\n\n"
            
            text "Creative Director\n" style "roll"
            text "Park Hyeong Rak\n"
            
            text "\nLead Programmer\n" style "roll"

            text "Jo Sang Hyeong\n"

            text "\nArt Director\n" style "roll"

            text "Kim Hyung Jun\n"

            text "\nAudio Director\n" style "roll"

            text "An Cho Won\n"
        
            text "\nProgrammers\n" style "roll"

            text "Choi Yeong In\n"
            text "Go Min Soo\n"
            text "Park Jae Hong\n"
            text "Song Gi Won\n"
            text "Yang Jun Young\n"
            text "Yu Yeong Gwan\n"
            
            text "\nArt\n" style "roll"

            text "Kim Min Jae\n"
            text "Son Seok Hyun\n"
            text "Song Gi Won\n"
    
            text "\nAudio\n" style "roll"

            text "Lee Gang Hae\n" 

            text "\nStory\n" style "roll"

            text "Lee Jae Seo\n"
            text "Lee Min Do\n"
            text "Song Gi Won\n"
            
            text "\nEnglish Translators\n" style "roll"
            
            text "Gang Mok Won\n"
            text "Moon Sun Woong\n"
            
            text "\nJapanese Translator\n" style "roll"

            text "Song Hyeon Seung\n"

label end:
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    return

label credits_end:
    stop music fadeout 2.0
    $ renpy.vibrate(1009.0)
    $ renpy.pause(2.0, hard=True)
    return

style title:
    xalign 0.5
    size 80
    color "#0099ff"

style credits_hbox:
    xalign 0.5
    ysize 30
    spacing 40

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5
    color "#FFFFFF"
    size 27
    
style roll:
    xalign 0.5
    bold True
    color "#FF7CFC"
    size 20
    
style director:
    xalign 0.5
    bold True
    size 40
    color "#FFD16B"
    
style leader:
    size 25
    color "#FFFFFF"