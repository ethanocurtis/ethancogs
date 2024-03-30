from .mcstatus import MinecraftCog

def setup(bot):
    bot.add_cog(MinecraftCog(bot))