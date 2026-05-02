class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "empty"
        encoded='~-'.join([i[::-1] for i in strs])
        return encoded

    def decode(self, s: str) -> List[str]:
        if s=="empty":
            return []
        decoded=[i[::-1] for i in s.split('~-')]
        return decoded
