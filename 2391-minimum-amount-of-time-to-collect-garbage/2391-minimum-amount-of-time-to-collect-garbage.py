class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p_stack, g_stack, m_stack=[], [], []
        p_reach, g_reach, m_reach = 0,0,0
        for idx, val in enumerate(garbage):
            p_counts = val.count('P')
            g_counts = val.count('G')
            m_counts = val.count('M')
            if idx==0:
                p_stack.append(p_counts)
                if p_counts:
                    p_reach = idx
                g_stack.append(g_counts)
                if g_counts:
                    g_reach = idx
                m_stack.append(m_counts)
                if m_counts:
                    m_reach = idx
            else:
                p_stack.append(p_counts+travel[idx-1])
                if p_counts:
                    p_reach = idx
                g_stack.append(g_counts+travel[idx-1])
                if g_counts:
                    g_reach = idx
                m_stack.append(m_counts+travel[idx-1])
                if m_counts:
                    m_reach = idx
        return sum([sum(p_stack[:p_reach+1]), sum(g_stack[:g_reach+1]), sum(m_stack[:m_reach+1])])