from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='ram')
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
    ]
    rand_num1 = random.randint(0,len(ramu) - 1)
    if message=='tukareta':
        await ctx.send(ramu[rand_num1])
    else:
        await ctx.send('疲れてるのか疲れてないのかはっきりしろよ')
    
    


bot.run(token)
