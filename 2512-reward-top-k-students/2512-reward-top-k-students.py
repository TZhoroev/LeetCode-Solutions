class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        points = defaultdict(lambda: 0)
        for i in range(len(student_id)):
            student = student_id[i]
            words = report[i].split()
            print(words)
            for word in words:
                if word in positive_feedback:
                    points[student] += 3
                elif word in negative_feedback:
                    points[student] -= 1
                else: points[student] += 0
        heap = [(-score, student) for student, score in points.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[-1] for _ in range(k)]
    