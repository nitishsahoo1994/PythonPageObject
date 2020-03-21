from properties.p import Property


class FileLib:
    def getPropertyFile(self,key):
        prop = Property()
        disc_prop = prop.load_property_files("F:\selenium\PageObjectModule\config.properties")
        value = disc_prop.get(key)
        return value




