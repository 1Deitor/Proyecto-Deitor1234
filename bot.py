import discord
import aiohttp
import datetime
from discord.ext import commands
#from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! Soy {bot.user} un bot!')

@bot.command()
async def imagenes(ctx,*,query):
    """Busca una imagen basada en tu consulta y la envía."""
    search_url = f"https://serpapi.com/search.json?q={query}&tbm=isch&ijn=0&api_key=b76f388bb18805c07a29e5d023c6ca816878fd50ad5f190374c25a970cb607c3"
    await ctx.send(f"Dame unos segundos,¿esta es la imagen que estabas buscando👻?")

    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    # Obtén el primer resultado de la búsqueda
                    image_url = data['images_results'][0]['original']
                    await ctx.send(image_url)
                except (KeyError, IndexError):
                    await ctx.send("No encontré imágenes para eso, pa.")
            else:
                await ctx.send("Hubo un error buscando la imagen.")

@bot.command()
async def tiempo(ctx):
    ahora = datetime.datetime.now()
    await ctx.send(f"Aqui esta la fecha y hora del dia de hoy, espero que te guste🥳 \nFecha: {ahora.strftime('%d/%m/%Y')}\nHora: {ahora.strftime('%H:%M:%S')}")

@bot.command()
async def calcular(ctx, num1: float, operador: str, num2: float):
    """
    Realiza operaciones matemáticas básicas (suma, resta, multiplicación, división).
    Uso: !calcular <num1> <operador> <num2>
    """
    try:
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                await ctx.send("❌ No se puede dividir entre cero.")
                return
        else:
            await ctx.send("❌ Operador inválido. Usa +, -, * o /.")
            return

        await ctx.send(f"✅ El resultado de `{num1} {operador} {num2}` es: `{resultado}`")
    except Exception as e:
        await ctx.send(f"❌ Hubo un error al realizar el cálculo: {e}")

@bot.command()
async def dividir(ctx, *, operacion: str):
    """
    Realiza operaciones básicas: suma, resta, multiplicación y división.
    Uso: !calcular <operación>
    Ejemplo: !calcular 6 / 2
    """
    try:
        # Evalúa la operación de forma segura
        resultado = eval(operacion, {"__builtins__": None}, {})
        await ctx.send(f"El resultado de `{operacion}` es: `{resultado}`")
    except ZeroDivisionError:
        await ctx.send("Error: No se puede dividir entre cero.")
    except Exception as e:
        await ctx.send(f"Hubo un error al realizar la operación: {e}")

@bot.command()
async def listar_comandos(ctx):
    """
    Lista todos los comandos disponibles del bot.
    Uso: !comandos
    """
    comandos = [f"!{command}" for command in bot.commands]
    comandos_str = "\n".join(comandos)
    await ctx.send(f"**Comandos disponibles:**\n{comandos_str}")

