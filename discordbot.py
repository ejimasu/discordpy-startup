from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='r')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def hibiki(ctx,message='tukareta'):
    ramu = [
        'まだ終わってねえんだよ。',
        '死が救済な訳ないだろ',
        'こんな戦況からでも勝てるのが僕ら',
        '死体撃ちする奴がいるとゲームが楽しくなくなる。',
        'Valorantに全てを賭けれるのかよ',
        '動画見た。リロードの最中に逃げろよ。と思うのは俺がFPSに慣れてるからか？\n銃声で即座に敵の位置を確認、遮蔽物を利用してのタイミングを計った立ち回り\nうずくまってて撃たれてる連中は馬鹿としか言いようがないよ\nでも流石に一般人に要求するのは酷か',
        'BOTから出ろよ',
        '完全にバグでしょこれ、バグってるわこれ',
        'よぅしトイレ行ってくる',
        '楽しまなきゃ意味ないでしょ',
        'なｎ、なんかあかあｋあかいひげ、みたいなのが生えてるこれ',
        'おかしいだろ',
        '助けてkazu channel',
        'ただ単純なASOBI',
        'なんで俺の声が暁に聞こえるん',
        'なんでアンレートで降参しなきゃいけないんですかね',
        'ゆうたの心臓投げつけよう（提案）',
        'トレイターじゃなくてもああいう説明するでしょ、あれはないでしょ普通に',
        'このクソゲーがよぉ！！！！！！！！！！',
        '俺はラズベリーパイしかできない',
        'ヒロックはっし～ん',
        'もっと自信を持っていけよ',
        
        
        
    ]
 
    rand_num1 = random.randint(0,len(ramu) - 1)
    if message=='tukareta':
        await ctx.send(ramu[rand_num1])
    else:
        await ctx.send('疲れてるのか疲れてないのかはっきりしろよ')
@bot.command()
async def hirama(ctx):
    hira = [
            '殺してくれ',
            '頼むから',
            'あの子マジでよかったわ',
            '許してください',
            'ぼくは病気です',
            'やめてくれやめてくれ',
            'ミュートとか言うな',
            '滑るとか言うな',
            'まあ、良いことがあったときは誰かに話したくなりますからね',
        '辛いとかじゃなくて、速い',
        'ミスター河合塾',
        'あじゃ',
        '俺たちの青春は今始まったところだから',
        
           
           
           
    ]
    rand_num2 = random.randint(0,len(hira) - 1)
    await ctx.send(hira[rand_num2])
    
    


bot.run(token)
