from point import Point


class Curve:
    _curve_lookup = {}

    """
    p = prime
    a = element in the field specified by p
    b = same as above
    n = order of base point g of the curve
    gx = x coordinate of g
    gy = y coordinate of g
    """

    def __init__(self, name, p, a, b, n, gx, gy, cid):
        self.name = name
        self.p = p
        self.a = a
        self.b = b
        self.n = n
        self.gx = gx
        self.gy = gy
        self.cid = cid
        self._curve_lookup[cid] = self

    def pointOnCurve(self, x, y):
        left = y * y
        right = (x * x * x) + (self.a * x) + self.b
        return (left - right) % self.p == 0

    @classmethod
    def get_Curve(cls, cid):
        return cls._curve_lookup.get(cid)

    @property
    def G(self):
        return Point(self.gx, self.gy, self)

    @property
    def P(self):
        return self.p

    @property
    def Name(self):
        return self.name


# NIST-Curves
P192 = Curve(
    "P192",
    6277101735386680763835789423207666416083908700390324961279,
    -3,
    2455155546008943817740293915197451784769108058161191238065,
    6277101735386680763835789423176059013767194773182842284081,
    602046282375688656758213480587526111916698976636884684818,
    174050332293622031404857552280219410364023488927386650641,
    "nist_P-192"
    )

P256 = Curve(
    "P256",
    115792089210356248762697446949407573530086143415290314195533631308867097853951,
    -3,
    41058363725152142129326129780047268409114441015993725554835256314039467401291,
    115792089210356248762697446949407573529996955224135760342422259061068512044369,
    48439561293906451759052585252797914202762949526041747995844080717082404635286,
    36134250956749795798585127919587881956611106672985015071877198253568414405109,
    "nist_P_256"
    )

# Brainpool-Curves
brainpoolP160 = Curve(
    "brainpoolP160",
    int("0xE95E4A5F737059DC60DFC7AD95B3D8139515620F", 16),
    int("0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300", 16),
    int("0x1E589A8595423412134FAA2DBDEC95C8D8675E58", 16),
    int("0xE95E4A5F737059DC60DF5991D45029409E60FC09", 16),
    int("0xBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3", 16),
    int("0x1667CB477A1A8EC338F94741669C976316DA6321", 16),
    "brainpool_P160"
    )

brainpoolP192 = Curve(
    "brainpoolP192",
    int("0xC302F41D932A36CDA7A3463093D18DB78FCE476DE1A86297", 16),
    int("0x6A91174076B1E0E19C39C031FE8685C1CAE040E5C69A28EF", 16),
    int("0x469A28EF7C28CCA3DC721D044F4496BCCA7EF4146FBF25C9", 16),
    int("0xC302F41D932A36CDA7A3462F9E9E916B5BE8F1029AC4ACC1", 16),
    int("0xC0A0647EAAB6A48753B033C56CB0F0900A2F5C4853375FD6", 16),
    int("0x14B690866ABD5BB88B5F4828C1490002E6773FA2FA299B8F", 16),
    "brainpool_P192"
    )

brainpoolP256 = Curve(
    "brainpoolP256",
    int("0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377", 16),
    int("0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9", 16),
    int("0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6", 16),
    int("0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7", 16),
    int("0x8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262", 16),
    int("0x547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997", 16),
    "brainpool_P192"
    )

# SECG-Cures
secp192k1 = Curve(
    "secp192k1",
    int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFEE37", 16),
    int("0x000000000000000000000000000000000000000000000000", 16),
    int("0x000000000000000000000000000000000000000000000003", 16),
    int("0xFFFFFFFFFFFFFFFFFFFFFFFE26F2FC170F69466A74DEFD8D", 16),
    int("0xDB4FF10EC057E9AE26B07D0280B7F4341DA5D1B1EAE06C7D", 16),
    int("0x9B2F2F6D9C5628A7844163D015BE86344082AA88D95E2F9D", 16),
    "secp_192_k1"
    )

secp256k1 = Curve(
    "secp256k1",
    int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16),
    int("0x0000000000000000000000000000000000000000000000000000000000000000", 16),
    int("0x0000000000000000000000000000000000000000000000000000000000000007", 16),
    int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16),
    int("0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16),
    int("0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16),
    "secp_256_k1"
    )